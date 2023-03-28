#!/usr/bin/env python3

TEMP_XML_FILE = "/tmp/xmlapioutput.xml"
DEVICE_LIST_FILE = "./devicelist.csv"

def ReadDevices(device_list_file = DEVICE_LIST_FILE):

    from os import path

    devices = []

    PWD = path.realpath(path.dirname(__file__))
    device_list_file = path.join(PWD, device_list_file)

    fh = open(device_list_file, "r")
    while fh:
        line = fh.readline().rstrip()
        if line:
            [hostname, api_key] = line.split(",")
            devices.append({'hostname': hostname, 'api_key': api_key})
        else:
            break
    fh.close()

    return devices

def MakeXMLAPICall(hostname, api_key, cli_command):

    from subprocess import Popen, PIPE, check_output, getstatusoutput, STDOUT
    from os import path

    # Location of panxapi.py 
    panxapi_location = "pan-python-0.16.0/bin/panxapi.py"

    xml_command = ""
    words = cli_command.split(" ")
    for i in range(len(words)):
        xml_command += "<"+ words[i] +">"
    for i in range(len(words)-1, -1,-1):
        xml_command += "</"+ words[i] +">"

    PWD = path.realpath(path.dirname(__file__))
    panxapi_location = path.join(PWD, panxapi_location)

    api_command = "{} -h {} -K \"{}\" -x -o \"{}\"".format(panxapi_location, hostname, api_key, xml_command)

    try:
        process = Popen(api_command, stdout=PIPE, stderr=PIPE, shell=True)
        stdout = process.stdout.read()
        stderr = process.stderr.read()
    except Exception as e:
        quit("Subprocess command failed:", stderr.decode("utf-8"))

    # Write to temp file
    if stdout:
        lines = stdout.decode("utf-8").splitlines()
    else:
        quit("Subprocess command failed:", stderr.decode("utf-8"))

    #lines = output.splitlines()
    fh = open(TEMP_XML_FILE, "w")
    try:
        for line in lines:
            fh.write(line + "\n")
    finally:
        fh.close()

def ReadXMLFile():

    import xml.etree.ElementTree
    from os import remove

    entries = []
    _ = xml.etree.ElementTree.iterparse(TEMP_XML_FILE, events=('end', ))

    for event, elem in _:
        if elem.tag == 'entry':
            entry = {}
            for child in elem.iter():

                try:
                    value = elem.find(child.tag).text
                    if value.isnumeric():
                        value = int(value)
                    else:
                        value = value.rstrip()
                except:
                    value = None

                if child.tag != "entry":
                    key = child.tag.replace("-", "_")
                    entry[key] = value

            entries.append(entry)

    # Cleanup Temp XML file
    remove(TEMP_XML_FILE)

    return entries

def GetData(params = {}):

    command = params.get('command', 'show_admins')
    device_name = params.get('device_name', '')

    command_list = {
       'show_routing_route': "Route Table",
       'show_vpn_ike-sa': "IKE SAs",
       'show_vpn_ipsec-sa': "IPSEC SAs",
       'show_global-protect-gateway_current-user': "GlobalProtect Sessions",
       'show_vpn_tunnel': "Configured VPN Tunnels",
       'show_admins': "Admin Sessions",
       'show_routing_protocol_bgp_peer': "BGP Peers",
       'show_routing_protocol_bgp_peer-group': "Configured BGP Peer-Groups",
       'show_routing_protocol_bgp_loc-rib': "BGP Local Rib",
       'show_routing_protocol_bgp_rib-out': "BGP Rib Out",
       'show_routing_protocol_bgp_rib-out-detail': "BGP Rib Out Detailed",
    }

    data = []

    if command == 'list_devices':
        devices = ReadDevices()
        for device in devices:
             data.append(dict(hostname = device['hostname']))
        return data

    if command == 'list_commands':

        for key, value in command_list.items():
              data.append({key: value})
        return data

    if not command in command_list:
        raise("Command not in command list")

    devices = ReadDevices()
    for _ in devices:
         if 'device_name' in params and _['hostname'] != device_name:
             continue
         cmd = command.replace("_", " ")
         MakeXMLAPICall(_['hostname'], _['api_key'], cmd)
         data.extend(ReadXMLFile())

    return data
