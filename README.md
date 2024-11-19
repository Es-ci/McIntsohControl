**McIntoshControl**
A rather rough and tumble but functional python program I wrote to have open loop control of my Mcintosh MC52 through the use of a ITach IP2SL Ethernet -> RS232 bridge and be able to use it with HomeAssistant through the use of the api RestCommands and HomeAssistants scripts to be accesible in the UI.


**Rest_Command Home Assistant configuration**
rest_command:
  mcintosh_power_on:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Power On"}'

  mcintosh_power_off:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Power Off"}'

  mcintosh_volume_up:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Volume Up"}'

  mcintosh_volume_down:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Volume Down"}'

  mcintosh_zone1_on:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Zone 1 On"}'

  mcintosh_zone1_off:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Zone 1 Off"}'

  mcintosh_zone2_on:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Zone 2 On"}'

  mcintosh_zone2_off:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Zone 2 Off"}'

  mcintosh_input_tv:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Input TV"}'

  mcintosh_input_phono:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Input Phono"}'

  mcintosh_input_usb:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Input USB"}'

  mcintosh_input_roon:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Input Roon"}'

  mcintosh_mute:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Mute"}'

  mcintosh_unmute:
    url: "http://serverIP:5001/mcintosh"
    method: POST
    headers:
      Content-Type: "application/json"
    payload: '{"command": "Unmute"}'


**HomeAssistance Scripts Configuration section:**


mcintosh_power_on:
  alias: "McIntosh Power On"
  sequence:
    - service: rest_command.mcintosh_power_on

mcintosh_power_off:
  alias: "McIntosh Power Off"
  sequence:
    - service: rest_command.mcintosh_power_off

mcintosh_volume_up:
  alias: "McIntosh Volume Up"
  sequence:
    - service: rest_command.mcintosh_volume_up

mcintosh_volume_down:
  alias: "McIntosh Volume Down"
  sequence:
    - service: rest_command.mcintosh_volume_down

mcintosh_zone1_on:
  alias: "McIntosh Zone 1 On"
  sequence:
    - service: rest_command.mcintosh_zone1_on

mcintosh_zone1_off:
  alias: "McIntosh Zone 1 Off"
  sequence:
    - service: rest_command.mcintosh_zone1_off

mcintosh_zone2_on:
  alias: "McIntosh Zone 2 On"
  sequence:
    - service: rest_command.mcintosh_zone2_on

mcintosh_zone2_off:
  alias: "McIntosh Zone 2 Off"
  sequence:
    - service: rest_command.mcintosh_zone2_off

mcintosh_input_tv:
  alias: "McIntosh Input TV"
  sequence:
    - service: rest_command.mcintosh_input_tv

mcintosh_input_phono:
  alias: "McIntosh Input Phono"
  sequence:
    - service: rest_command.mcintosh_input_phono

mcintosh_input_usb:
  alias: "McIntosh Input USB"
  sequence:
    - service: rest_command.mcintosh_input_usb

mcintosh_input_roon:
  alias: "McIntosh Input Roon"
  sequence:
    - service: rest_command.mcintosh_input_roon

mcintosh_mute:
  alias: "McIntosh Mute"
  sequence:
    - service: rest_command.mcintosh_mute

mcintosh_unmute:
  alias: "McIntosh Unmute"
  sequence:
    - service: rest_command.mcintosh_unmute
