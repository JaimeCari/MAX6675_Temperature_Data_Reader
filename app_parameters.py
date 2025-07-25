##################################################
# Listado de parámetros importantes del proyecto #
##################################################

BAUD_RATE = 9600
COMMAND_REQUEST_TEMP = b'T' # Modificar manualmente en .ino
COMMAND_SERVO_OPEN = b'O' # Modificar manualmente en .ino
COMMAND_SERVO_CLOSE = b'C' # Modificar manualmente en .ino
MAX_PLOT_POINTS = 100    
DATA_REQUEST_INTERVAL_MS = 200
APP_WINDOW_TITLE = "Monitor de Temperatura y Control de Servo"
TEMP_DISPLAY_STYLE = "font-size: 24px; font-weight: bold; color: red;"
TIME_DISPLAY_STYLE = "font-size: 18px; color: red;"
HELP_LABEL_STYLE = "color: gray; font-size: 10px; margin-left: 5px;"
CSV_HEADERS = ['Tiempo (s)', 'Temperatura (°C)', 'Estado Servo']
CSV_FILE_FILTER = "Archivos CSV (*.csv);;Todos los archivos (*.*)"
DEFAULT_CYCLE_COUNT = 5
DEFAULT_INTERVAL_SEC = 5.0
