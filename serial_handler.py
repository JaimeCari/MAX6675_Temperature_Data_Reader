# serial_handler.py (MODIFICADO)

import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal
import time

# Importar DATA_REQUEST_INTERVAL_MS ya no es necesario aquí.
# from app_params import DATA_REQUEST_INTERVAL_MS

class SerialReader(QThread):
    temperature_received = pyqtSignal(float)
    connection_status = pyqtSignal(bool, str)
    error_message = pyqtSignal(str)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.ser = None
        self._running = True
        
        # ELIMINAR EL QTimer de aquí
        # self.request_data_timer = QTimer()
        # self.request_data_timer.timeout.connect(self.request_data)
        
    def run(self):
        try:
            self.ser = serial.Serial(self.port, 9600, timeout=1) # 9600 baudios, timeout de 1 segundo
            if self.ser.isOpen():
                self.connection_status.emit(True, f"Conectado a {self.port}")
                # ELIMINAR EL INICIO DEL TIMER DE AQUÍ
                # self.request_data_timer.start(DATA_REQUEST_INTERVAL_MS)
                
                while self._running:
                    if self.ser.in_waiting > 0:
                        line = self.ser.readline().decode('utf-8').strip()
                        if line.startswith("Temp:"):
                            try:
                                temp_str = line.split(":")[1].strip().replace('C', '')
                                temperature = float(temp_str)
                                self.temperature_received.emit(temperature)
                            except ValueError:
                                self.error_message.emit(f"Dato de temperatura inválido: {line}")
                        # Pequeña pausa para no saturar la CPU si no hay datos
                        time.sleep(0.01) 
            else:
                self.connection_status.emit(False, f"No se pudo abrir el puerto {self.port}")

        except serial.SerialException as e:
            self.connection_status.emit(False, f"Error de conexión serial: {e}")
            self.error_message.emit(f"Error fatal serial: {e}")
        except Exception as e:
            self.connection_status.emit(False, f"Error inesperado en el hilo serial: {e}")
            self.error_message.emit(f"Error inesperado: {e}")
        finally:
            if self.ser and self.ser.isOpen():
                self.ser.close()
            self.connection_status.emit(False, f"Puerto {self.port} cerrado.")

    def stop(self):
        self._running = False
        # ELIMINAR LA PARADA DEL TIMER DE AQUÍ
        # if self.request_data_timer.isActive():
        #    self.request_data_timer.stop()
        self.wait() # Espera a que el hilo termine

    def send_command(self, command):
        """Envía un comando al Arduino."""
        if self.ser and self.ser.isOpen():
            try:
                self.ser.write(f"{command}\n".encode('utf-8'))
            except serial.SerialException as e:
                self.error_message.emit(f"Error al enviar comando: {e}")
        else:
            self.error_message.emit("No hay conexión serial para enviar comando.")

    # El método request_data se queda, pero será llamado desde el hilo principal
    def request_data(self):
        """Envía el comando 'T' para solicitar temperatura al Arduino."""
        self.send_command('T') # Asegúrate de que tu Arduino responde a 'T' con "Temp:XX.XX"

def list_available_ports():
    """Lista los puertos COM disponibles."""
    ports = serial.tools.list_ports.comports()
    return [p.device for p in ports]
