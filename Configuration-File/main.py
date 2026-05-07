from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

# Cargamos la configuracion
nr = InitNornir(config_file="config.yaml")

# Ejecutamos el comando en los 3 routers
resultado = nr.run(
    task=netmiko_send_command, 
    command_string="show ip interface brief"
)

# Mostramos el resultado en la terminal
print_result(resultado)
