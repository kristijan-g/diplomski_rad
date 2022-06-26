import random, sys, json

def generate_id(input2_data):
    flag = True
    while True:
        id = ""
        for i in range(36):
            if i == 8 or i == 13 or i == 18 or i == 23:
                id += "_"
            else:
                id += chr(random.randint(97, 122))
        for i in input2_data:
            if id in i["id"]:
                flag = False
        if flag is True:
            return id


departments = int(sys.argv[1])
workers_per_department = int(sys.argv[2])
av_to_turn_off = int(sys.argv[3])
input1 = open("D:\Downloads1\kg_diplomski1\ClientInfo.json", "r+")
input1_data = json.loads(input1.read())
input2 = open("D:\Downloads1\kg_diplomski1\Global.json", "r+")
input2_data = json.loads(input2.read())
output1 = open("ClientInfo.json", "w+")
output2 = open("Global.json", "w+")
output3 = open("Players.json", "w+")
startX = 3400
startY = 2500
actor_ids = []
depts = []
for d in range(departments):
    pc_id1 = []
    pc_id2 = []
    id = generate_id(input2_data)
    input2_data.append({"labels": ["organization"], "id": id, "name": "Zavod" + str(d + 4), "nodes": [{"labels": ["contract"], "name": "Vanjska organizacija", "organization_id": "vmrcuoth_ctof_lekb_wbsk_gnatsmupztqu", "provide_assistance": "contract", "incident_info_sharing": "contract", "infrastructure_info_sharing": "contract", "allow_audit": "contract"}], "reputation": 0, "is_attacked": False, "controls": [], "encryption_keys": [], "suspicious_machines": [], "phishing_warning_disabled": False, "natural_key": "Zavod" + str(d + 4)})
    depts.append({"labels": ["organization"], "id": id, "name": "Zavod" + str(d + 4), "nodes": [], "reputation": 0, "is_attacked": False, "controls": [], "encryption_keys": [], "suspicious_machines": [], "phishing_warning_disabled": False, "natural_key": "Zavod" + str(d + 4)})
    input1_data[0]["Objects"][id] = {"X": 1500 + (d * 100), "Y": -300, "IconPath": "/graphIcons/organization-40.png"}
    id1 = generate_id(input2_data)
    input2_data.append({"labels": ["physical_zone", "internal_zone"], "id": id1, "name": "Zavod" + str(d + 4), "physical_zone": "fnxpbplf_hosx_pilp_rcoq_twvduavwqqas", "controls": [], "natural_key": "Zavod" + str(d + 4)})
    input1_data[0]["Objects"][id1] = {"X": 0, "Y": 0, "IconPath": "/graphIcons/internal_zone-40cf02b5-da22-4b24-ae6e-91b93c309464.png"}
    for i in range(2):
        id2 = generate_id(input2_data)
        input2_data.append({"labels": ["internal_zone", "physical_zone"], "id": id2, "physical_zone": str(id1), "name": "Z" + str(d + 4) + "U" + str(i + 1), "controls": [], "natural_key": "Z" + str(d + 4) + "U" + str(i + 1)})
        input1_data[0]["Objects"][id2] = {"X": 0, "Y": 0, "IconPath": "/graphIcons/internal_zone-40cf02b5-da22-4b24-ae6e-91b93c309464.png"}
        if i == 0:
            num = random.randint(1, workers_per_department)
            for j in range(workers_per_department):
                id3 = generate_id(input2_data)
                id4 = generate_id(input2_data)
                input2_data.append({"labels": ["actor", "person"], "id": id3, "name": "Zaposlenik" + str(d + 4) + "_" + str(j + 1), "description": "", "skills": [], "organization_id": id, "physical_zone": id2, "work_stations": [id4], "vip": False, "publicly_exposed": 0.3, "mail": "zaposlenik" + str(d + 4) + "_" + str(j + 1) + "@zavod" + str(d + 4) + ".fakultet.hr", "emails_recieved_per_day": 3, "reads_mail_on": [id4], "accounts": [{"labels": ["user_account", "data"], "name": "zaposlenik" + str(d + 4) + "_" + str(j + 1) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "zaposlenik" + str(d + 4) + "_" + str(j + 1) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0, "is_hashed": False, "natural_key": "zaposlenik" + str(d + 4) + "_" + str(j + 1) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"}],"gathered_intelligence": [], "controls": [{"labels":["control", "securityawareness"], "name":"Security awareness", "awareness":0.5, "isactive":True, "mode":["log", "alert", "block"], "event_frequency":10}], "assets": [], "enable_messaging": False, "natural_key": "Zaposlenik" + str(d + 4) + "_" + str(j + 1)})
                input1_data[0]["Objects"][id3] = {"X": startX + (j * 150), "Y": startY, "IconPath": "/graphIcons/actor-000.png"}
                actor_ids.append(id3)
                input2_data.append({"labels": ["machine", "asset", "os", "file_system"], "id": id4, "name": "PC" + str(d + 4) + "_" + str(j + 1), "description": "", "organization_id": id, "physical_zone": id2, "is_on": True, "enables_routing": False, "logged_in": [], "availability": 1, "machine_id": id4, "remote_files": [], "protocols": ["smb:445", "rdp:3389"], "install_time": 0, "size": 0, "controls": [], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {"labels": ["proxy_config"], "name": "proxy_config", "machine_id": "", "protocols": ["https:443"], "natural_key": "proxy_config"}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 10, "software_info": "windows", "log_server_id": "", "marked_as_suspicious": False, "usually_accessed_by": [], "natural_key": "PC" + str(d + 4) + "_" + str(j + 1)})
                input1_data[0]["Objects"][id4] = {"X": startX + (j * 150), "Y": startY + 200, "IconPath": "/graphIcons/machine-0000.png"}
                pc_id1.append(id4)
            id4 = generate_id(input2_data)
            for l in range(len(input2_data)):
                if "_" in input2_data[l]["name"]:
                    if input2_data[l]["name"].split("_")[1][0] == str(num) and "PC" + str(d + 4) in input2_data[l]["name"]:
                        input2_data[l]["software_info"] = "ee1cd128_da42_4377_85a8_8060437f1512"
                        that_id = input2_data[l]["id"]
                        break
            input2_data.append({"labels": ["data_container", "file"], "id": id4, "name": "Ocjene" + str(d + 4), "file_system_id": that_id, "data": [{"labels": ["data", "generic_data"], "name": "Ocjene" + str(d + 4), "data_id": "ukeufphx_vagm_pbcg_bhmu_pxbpleccqezn", "quantity": 1, "range": "0-0", "natural_key": "ukeufphx_vagm_pbcg_bhmu_pxbpleccqezn"}], "encryption_keys": [], "integrity": True, "size": 0, "on_delete": [], "quarantined": False, "adverse_events": [], "natural_key": that_id + "Ocjene" + str(d + 4) + "ukeufphx_vagm_pbcg_bhmu_pxbpleccqezn"})
            input1_data[0]["Objects"][id4] = {"X": 0, "Y": 0, "IconPath": "/graphIcons/file-17.png"}
        else:
            for j in range(3):
                id3 = generate_id(input2_data)
                id4 = generate_id(input2_data)
                if j == 0:
                    input2_data.append({"labels": ["actor", "person"], "id": id3, "name": "Tajnica" + str(d + 4), "description": "", "skills": [], "organization_id": id, "physical_zone": id2, "work_stations": [id4], "vip": False, "publicly_exposed": 0.5, "mail": "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "emails_recieved_per_day": 5, "reads_mail_on": [id4], "accounts": [{"labels": ["user_account", "data"], "name": "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0, "is_hashed": False, "natural_key": "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"}],"gathered_intelligence": [], "controls": [{"labels": ["control", "securityawareness"], "name": "Security awareness", "awareness": 0, "isactive": True, "mode": ["log", "alert", "block"], "event_frequency": 10}], "assets": [], "enable_messaging": False, "natural_key": "Tajnica" + str(d + 4)})
                    input1_data[0]["Objects"][id3] = {"X": startX + (j * 150) + (workers_per_department * 200), "Y": startY, "IconPath": "/graphIcons/actor-5.png"}
                    id3_1 = generate_id(input2_data)
                    input2_data.append({"labels": ["data_container", "file"], "id": id3_1, "name": "Osobni podaci djelatnika Zavoda" + str(d + 4), "file_system_id": id3, "data": [{"labels": ["data", "generic_data"], "name": "Osobni podaci djelatnika Zavoda" + str(d + 4), "data_id": "Osobni podaci djelatnika Zavoda" + str(d + 4), "quantity": 1, "range": "0-0"}], "encryption_keys": [], "integrity": True, "size": 0, "on_delete": [], "quarantined": False, "adverse_events": []})
                    input1_data[0]["Objects"][id3_1] = {"X": 0, "Y": 0, "IconPath": "/graphIcons/file-17.png"}
                    actor_ids.append(id3)
                elif j == 1:
                    input2_data.append({"labels": ["actor", "person"], "id": id3, "name": "Predstojnik" + str(d + 4), "description": "", "skills": [], "organization_id": id, "physical_zone": id2, "work_stations": [id4], "vip": False, "publicly_exposed": 1, "mail": "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "emails_recieved_per_day": 10, "reads_mail_on": [id4], "accounts": [{"labels": ["user_account", "data"], "name": "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0, "is_hashed": False, "natural_key": "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"}],"gathered_intelligence": [], "controls": [{"labels": ["control", "securityawareness"], "name": "Security awareness", "awareness": 1, "isactive": True, "mode": ["log", "alert", "block"], "event_frequency": 10}], "assets": [], "enable_messaging": False, "natural_key": "Predstojnik" + str(d + 4)})
                    input1_data[0]["Objects"][id3] = {"X": startX + (j * 150) + (workers_per_department * 200), "Y": startY, "IconPath": "/graphIcons/actor-6.png"}
                    actor_ids.append(id3)
                elif j == 2:
                    input2_data.append({"labels": ["actor", "person"], "id": id3, "name": "SysAdmin" + str(d + 4), "description": "", "skills": [{"labels": ["skill", "system_administration"], "name": "System administration", "value": 1, "natural_key": "System administration"}], "organization_id": id, "physical_zone": id2, "work_stations": [id4], "vip": False, "publicly_exposed": 0, "mail": "sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "emails_recieved_per_day": 5, "reads_mail_on": [id4], "accounts": [{"labels": ["user_account", "data"], "name": "sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0, "is_hashed": False, "natural_key": "sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"}],"gathered_intelligence": [], "controls": [{"labels": ["control", "securityawareness"], "name": "Security awareness", "awareness": 1, "isactive": True, "mode": ["log", "alert", "block"], "event_frequency": 10}], "assets": [], "enable_messaging": True, "natural_key": "SysAdmin" + str(d + 4)})
                    input1_data[0]["Objects"][id3] = {"X": startX + (j * 150) + (workers_per_department * 200), "Y": startY, "IconPath": "/graphIcons/actor-3.png"}
                    actor_ids.append(id3)
                input2_data.append({"labels": ["machine", "asset", "os", "file_system"], "id": id4, "name": "PC" + str(d + 4) + "_" + str(j + workers_per_department + 1), "description": "", "organization_id": id, "physical_zone": id2, "is_on": True, "enables_routing": False, "logged_in": [], "availability": 1, "machine_id": id4, "remote_files": [], "protocols": ["https:443", "smb:445", "smtp:25", "rdp:3389", "imap:143"], "install_time": 0, "size": 0, "controls": [], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {"labels": ["proxy_config"], "name": "proxy_config", "machine_id": "", "protocols": ["https:443"], "natural_key": "proxy_config"}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 10, "software_info": "windows", "log_server_id": "", "marked_as_suspicious": False, "usually_accessed_by": [], "natural_key": "PC" + str(d + 4) + "_" + str(j + 1)})
                input1_data[0]["Objects"][id4] = {"X": startX + (j * 150) + (workers_per_department * 200), "Y": startY + 200, "IconPath": "/graphIcons/machine-0000.png"}
                pc_id2.append(id4)
    id5 = generate_id(input2_data)
    input2_data.append({"labels": ["machine", "asset", "os", "file_system"], "id": id5, "name": "Backup server" + str(d + 4), "description": "", "organization_id": id, "physical_zone": id1, "is_on": True, "enables_routing": False, "log_server_id": "", "logged_in": [], "marked_as_suspicious": False, "usually_accessed_by": [], "availability": 1, "machine_id": id5, "remote_files": [], "protocols": [], "install_time": 0, "size": 0, "controls": [], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 0, "software_info": "", "natural_key": "Backup server" + str(d + 4)})
    input1_data[0]["Objects"][id5] = {"X": startX - 400, "Y": startY + 400, "IconPath": "/graphIcons/machine-9ee84e0c-9d2c-4df1-b204-d2044c71c45e.png"}
    id6 = generate_id(input2_data)
    input2_data.append({"labels": ["asset", "machine", "os", "file_system"], "id": id6, "name": "Proxy server" + str(d + 4), "description": "", "organization_id": id, "physical_zone": id1, "is_on": True, "enables_routing": False, "log_server_id": "", "logged_in": [], "marked_as_suspicious": False, "usually_accessed_by": [], "availability": 1, "machine_id": id6, "remote_files": [], "protocols": [], "install_time": 0, "size": 0, "controls": [{"labels": ["control", "webproxy"], "name": "Web proxy", "isactive": True, "mode": ["log"], "event_frequency": 1, "blacklist": [], "natural_key": "Web proxy"}], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 0, "software_info": "", "natural_key": "Proxy server" + str(d + 4)})
    input1_data[0]["Objects"][id6] = {"X": startX - 500, "Y": startY + 600, "IconPath": "/graphIcons/machine-0000.png"}
    id7 = generate_id(input2_data)
    input2_data.append({"labels": ["machine", "asset", "os", "file_system"], "id": id7, "name": "Active directory" + str(d + 4), "description": "", "organization_id": id, "physical_zone": id1, "is_on": True, "enables_routing": False, "logged_in": [], "availability": 1, "machine_id": id7, "remote_files": [], "protocols": [], "install_time": 0, "size": 0, "controls": [], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 0, "software_info": "", "natural_key": "Active directory" + str(d + 4), "log_server_id": "", "marked_as_suspicious": False, "usually_accessed_by": []})
    input1_data[0]["Objects"][id7] = {"X": startX - 600, "Y": startY + 800, "IconPath": "/graphIcons/machine-0000.png"}
    id8 = generate_id(input2_data)
    input2_data.append({"labels": ["machine", "asset", "os", "file_system"], "id": id8, "name": "Database server" + str(d + 4), "description": "", "organization_id": id, "physical_zone": id1, "is_on": True, "enables_routing": False, "log_server_id": "", "logged_in": [], "marked_as_suspicious": False, "usually_accessed_by": [], "availability": 1, "machine_id": id8, "remote_files": [], "protocols": [], "install_time": 0, "size": 0, "controls": [], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 0, "software_info": "", "natural_key": "Database server" + str(d + 4)})
    input1_data[0]["Objects"][id8] = {"X": startX - 700, "Y": startY + 1000, "IconPath": "/graphIcons/machine-a0f3019b-a203-4200-9e30-7e52116c0dab.png"}
    id9 = generate_id(input2_data)
    input2_data.append({"labels": ["machine", "asset", "os", "file_system"], "id": id9, "name": "DNS" + str(d + 4), "description": "", "organization_id": id, "physical_zone": id1, "is_on": True, "enables_routing": False, "log_server_id": "", "logged_in": [], "marked_as_suspicious": False, "usually_accessed_by": [], "availability": 1, "machine_id": id9, "remote_files": [], "protocols": [], "install_time": 0, "size": 0, "controls": [], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 0, "software_info": "", "natural_key": "DNS" + str(d + 4)})
    input1_data[0]["Objects"][id9] = {"X": startX + 1300, "Y": startY + 700, "IconPath": "/graphIcons/machine-cb041795-a24d-4d6e-acea-be7a80cc284e.png"}
    id10 = generate_id(input2_data)
    input2_data.append({"labels": ["dns", "service", "software", "file"], "name": "DNS" + str(d + 4), "id": id10, "soa_for_domains": [], "description": "", "file_system_id": id9, "organization_id": id, "resource_records": [], "parent_dns": "", "encryption_keys": [], "autorun": True, "is_installed": True, "is_running": True, "logged_in": [], "accounts": [], "availability": 1, "controlled_by": "", "control_protocol": "", "control_direction": "", "running_under_account": "SYSTEM", "used_data_containers": [], "protocols": ["dns:53"], "adverse_events": [], "usually_accessed_by": [], "integrity": True, "size": 0, "on_delete": [], "quarantined": False, "functionalities": [], "controls": [{"labels": ["control", "dnsblacklist"], "name": "DNS Blacklist", "isactive": True, "mode": ["log", "block"], "event_frequency": 10, "blacklist": [], "natural_key": "DNS Blacklist"}], "required_os": "", "install": {}, "run": {}, "memory": [], "software_version": 0, "software_patch_date": 1577836800000, "software_info": "d773ac31_42dc_4dd2_b9e1_0975ae6a33f2", "natural_key": id9 + "DNS" + str(d + 4) + "0Truedns:53SYSTEM"})
    input1_data[0]["Objects"][id10] = {"X": 0, "Y": 0, "IconPath": "/graphIcons/file-17.png"}
    id12 = generate_id(input2_data)
    input2_data.append({"labels": ["asset", "file_system", "machine", "os", "mail_server", "service", "software", "file"], "id": id12, "name": "Mail server" + str(d + 4), "description": "", "file_system_id": id12, "organization_id": id, "physical_zone": id1, "encryption_keys": [], "is_on": True, "enables_routing": False, "log_server_id": "", "logged_in": [], "marked_as_suspicious": False, "machine_id": id12, "remote_files": [], "usually_accessed_by": [], "availability": 1, "autorun": False, "is_installed": False, "is_running": False, "accounts": [], "protocols": ["smtp:25", "pop3:110", "imap:143", "rdp:3389", "smtp_ssl:465", "pop3_ssl:995", "imap_ssl:993"], "controlled_by": "", "control_protocol": "", "control_direction": "", "install_time": 0, "running_under_account": "SYSTEM", "used_data_containers": [], "size": 0, "adverse_events": [], "controls": [], "functionalities": [], "domains": ["zavod" + str(d + 4) + ".fakultet.hr"], "integrity": True, "on_delete": [], "quarantined": False, "proxy_config": {}, "required_os": "", "install": {}, "run": {}, "memory": [], "software_patch_date": 1577836800000, "software_version": 0, "software_info": "", "natural_key": id12 + "Mail server" + str(d + 4) + "0Falsesmtp:25pop3:110imap:143rdp:3389smtp_ssl:465pop3_ssl:995imap_ssl:993SYSTEM"})
    input1_data[0]["Objects"][id12] = {"X": startX + 1300, "Y": startY + 500, "IconPath": "/graphIcons/machine-6e1f7a9c-22cc-4f34-a6ca-4eddbe0b7a99.png"}
    id13 = generate_id(input2_data)
    input2_data.append({"labels": ["machine", "asset", "os", "file_system"], "id": id13, "name": "FW" + str(d + 4), "description": "", "organization_id": id, "physical_zone": id1, "is_on": True, "enables_routing": False, "log_server_id": "", "logged_in": [], "marked_as_suspicious": False, "usually_accessed_by": [], "availability": 1, "machine_id": id13, "remote_files": [], "protocols": ["https:443", "smtp:25", "smtp_ssl:465", "imap:143", "imap_ssl:993", "pop3:110", "pop3_ssl:995", "ssh:22", "pptp:1723"], "install_time": 0, "size": 0, "controls": [], "controlled_by": "", "control_protocol": "", "control_direction": "", "functionalities": [], "accounts": [], "proxy_config": {}, "adverse_events": [], "memory": [], "software_patch_date": 1577836800000, "software_version": 0, "software_info": "", "natural_key": "FW" + str(d + 4)})
    input1_data[0]["Objects"][id13] = {"X": startX + 550, "Y": startY + 900, "IconPath": "/graphIcons/machine-5eb11175-4d44-49b1-a468-490d99062527.png"}
    id14 = generate_id(input2_data)
    input2_data.append({"labels": ["trust_zone"], "id": id14, "name": "LAN interne usluge" + str(d + 4), "organization_id": id, "resources": [id5, id6, id7, id8, id13], "hop_count": 0, "natural_key": "LAN interne usluge" + str(d + 4)})
    input1_data[0]["Objects"][id14] = {"X": startX - 250, "Y": startY + 750, "IconPath": "/graphIcons/trust_zone-0000.png"}
    id15 = generate_id(input2_data)
    input2_data.append({"labels": ["trust_zone"], "id": id15, "name": "DMZ" + str(d + 4), "organization_id": id, "resources": [id9, id12, id13], "hop_count": 0, "natural_key": "DMZ" + str(d + 4)})
    input1_data[0]["Objects"][id15] = {"X": startX + 1100, "Y": startY + 600, "IconPath": "/graphIcons/trust_zone-0000.png"}
    id16 = generate_id(input2_data)
    input2_data.append({"labels": ["trust_zone"], "id": id16, "name": "LAN Z" + str(d + 4) + "U1", "organization_id": id, "resources": [id for id in pc_id1] + [id13], "hop_count": 0, "natural_key": "LAN Z" + str(d + 4) + "U" + str(i + 1)})
    input1_data[0]["Objects"][id16] = {"X": startX + 150, "Y": startY + 550, "IconPath": "/graphIcons/trust_zone-0000.png"}
    id17 = generate_id(input2_data)
    input2_data.append({"labels": ["trust_zone"], "id": id17, "name": "LAN Z" + str(d + 4) + "U2", "organization_id": id, "resources": [id for id in pc_id2] + [id13], "hop_count": 0, "natural_key": "LAN Z" + str(d + 4) + "U" + str(i + 1)})
    input1_data[0]["Objects"][id17] = {"X": startX + 750, "Y": startY + 550, "IconPath": "/graphIcons/trust_zone-0000.png"}
    id18 = generate_id(input2_data)
    input2_data.append({"labels": ["file", "data_container"], "id": id18, "name": "Auth server credential store Z" + str(d + 4), "file_system_id": id7, "data": [{"labels": ["data", "user_account"], "name": "zaposlenik" + str(d + 4) + "_" + str(w + 1) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "zaposlenik" + str(d + 4) + "_" + str(w + 1) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0.8, "is_hashed": False, "natural_key": "zaposlenik" + str(d + 4) + "_" + str(w + 1) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"} for w in range(workers_per_department)] + [{"labels": ["data", "user_account"], "name": "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0.8, "is_hashed": False, "natural_key": "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"}, {"labels": ["data", "user_account"], "name": "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0.8, "is_hashed": False, "natural_key": "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"}, {"labels": ["data", "user_account"], "name": "sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "user_account_id": "sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "frequency": 0, "last_changed": 1577836800000, "disabled": False, "quality": 0.8, "is_hashed": False, "natural_key": "sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"}], "encryption_keys": [], "integrity": True, "size": 0, "on_delete": [], "quarantined": False, "adverse_events": [], "natural_key": id7 + "Auth server credential store Z" + str(d + 4) + "0" + "".join(["zaposlenik" + str(d + 4) + "_" + str(w + 1) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM" for w in range(workers_per_department)]) + "tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AMpredstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AMsysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr1/1/2020 12:00:00 AM"})
    input1_data[0]["Objects"][id18] = {"X": 0, "Y": 0, "IconPath": "/graphIcons/file-17.png"}
    id19 = generate_id(input2_data)
    input2_data.append({"labels": ["user_group"], "id": id19, "name": "Domain Users Z" + str(d + 4), "user_account_ids": ["zaposlenik" + str(d + 4) + "_" + str(w + 1) + "@zavod" + str(d + 4) + ".fakultet.hr" for w in range(workers_per_department)] + ["tajnica" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr", "predstojnik" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr"], "user_groups": [], "organization_id": id, "natural_key": "Domain Users Z" + str(d + 4)})
    input1_data[0]["Objects"][id19] = {"X": startX + 150, "Y": startY + 1200, "IconPath": "/graphIcons/unknown.png"}
    id20 = generate_id(input2_data)
    input2_data.append({"labels": ["user_group"], "id": id20, "name": "Domain Admin Z" + str(d + 4), "user_account_ids": ["sysadmin" + str(d + 4) + "@zavod" + str(d + 4) + ".fakultet.hr"], "user_groups": [], "organization_id": id, "natural_key": "Domain Admin Z" + str(d + 4)})
    input1_data[0]["Objects"][id20] = {"X": startX + 300, "Y": startY + 1200, "IconPath": "/graphIcons/unknown.png"}
    id21 = generate_id(input2_data)
    pc_id = pc_id1 + pc_id2
    input2_data.append({"labels": ["group"], "id": id21, "machine_id": id7, "name": "AAA grupa Z" + str(d + 4), "members": [id for id in pc_id] + [id5, id6, id7, id8, id9, id12, id13], "controls": [{"labels": ["control", "aaa"], "name": "AAA", "isactive": True, "mode": ["log"], "event_frequency": 10, "remotecredentialstore": id18, "localcredentialstore": "", "authorizations": [{"labels": ["authorization"], "name": "Domain admin", "user_account_id": "", "user_group_id": id20, "login_privilege": "admin", "natural_key": "Domain admin"}, {"labels": ["authorization"], "name": "Domain user", "user_account_id": "", "user_group_id": id19, "login_privilege": "user", "natural_key": "Domain user"}], "file_access_rules": []}]})
    input1_data[0]["Objects"][id21] = {"X": startX + 450, "Y": startY + 1200, "IconPath": "/graphIcons/group-b9f05bf3-65db-40c8-bf76-7e490476eb5d.png"}
    id22 = generate_id(input2_data)
    input2_data.append({"labels": ["group"], "id": id22, "machine_id": id7, "name": "AV grupa Z" + str(d + 4), "members": [id for id in pc_id] + [id5, id6, id7, id8, id9, id12], "controls": []})
    input1_data[0]["Objects"][id22] = {"X": startX + 600, "Y": startY + 1200, "IconPath": "/graphIcons/group-b9f05bf3-65db-40c8-bf76-7e490476eb5d.png"}
    for k in range(len(input2_data)):
        if "Intranet" in input2_data[k]["name"]:
            intra_id = input2_data[k]["id"]
        if "FW " + str(d + 4) in input2_data[k]["name"]:
            input2_data[k]["controls"] = [{"labels": ["control", "firewall"], "name": "Firewall", "isactive": True, "mode": ["log", "block"], "event_frequency": 50, "rules": [{"labels": ["fw_rule"], "name": "LAN_Z" + str(d + 4) + "U1_Proxy_server" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": id16, "outgoing_via_interface": "", "any_interface_outgoing": False, "destination": id6, "protocols": ["https:443"], "natural_key": "LAN_Z" + str(d + 4) + "U1_Proxy_server" + str(d + 4)}, {"labels": ["fw_rule"], "name": "LAN_Z" + str(d + 4) + "U2_Proxy_server" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": id17, "outgoing_via_interface": "", "any_interface_outgoing": False, "destination": id6, "protocols": ["https:443"], "natural_key": "LAN_Z" + str(d + 4) + "U2_Proxy_server" + str(d + 4)}, {"labels": ["fw_rule"], "name": "Proxy_server" + str(d + 4) + "_Intranet", "isactive": True, "fw_rule_mode": "allow", "source": id6, "any_interface_incoming": False, "incoming_via_interface": "", "outgoing_via_interface": "saiygvlo_vfqv_cdrw_vgaj_lnboivkiwlpv", "any_interface_outgoing": False, "destination": "", "protocols": ["https:443"], "natural_key": "Proxy_server" + str(d + 4) + "_Intranet"}, {"labels": ["fw_rule"], "name": "LAN_Z" + str(d + 4) + "U1_Mail_server" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": id16, "outgoing_via_interface": "", "any_interface_outgoing": False, "destination": id12, "protocols": ["pop3:110", "imap:143", "smtp:25", "pop3_ssl:995", "imap_ssl:993", "smtp_ssl:465"], "natural_key": "LAN_Z" + str(d + 4) + "U1_Mail_server" + str(d + 4)}, {"labels": ["fw_rule"], "name": "LAN_Z" + str(d + 4) + "U2_Mail_server" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": id17, "outgoing_via_interface": "", "any_interface_outgoing": False, "destination": id12, "protocols": ["pop3:110", "imap:143", "smtp:25", "pop3_ssl:995", "imap_ssl:993", "smtp_ssl:465"], "natural_key": "LAN_Z" + str(d + 4) + "U2_Mail_server" + str(d + 4)}, {"labels": ["fw_rule"], "name": "Intranet_Proxy_server" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": "saiygvlo_vfqv_cdrw_vgaj_lnboivkiwlpv", "outgoing_via_interface": "", "any_interface_outgoing": False, "destination": id6, "protocols": ["https:443"], "natural_key": "Intranet_Proxy_server" + str(d + 4)}, {"labels": ["fw_rule"], "name": "LAN_Z" + str(d + 4) + "U1_LAN_interne_usluge" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": id16, "outgoing_via_interface": id14, "any_interface_outgoing": False, "destination": "", "protocols": ["http:80", "https:443"], "natural_key": "LAN_Z" + str(d + 4) + "U1_LAN_interne_usluge" + str(d + 4)}, {"labels": ["fw_rule"], "name": "LAN_Z" + str(d + 4) + "U2_LAN_interne_usluge" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": id17, "outgoing_via_interface": id14, "any_interface_outgoing": False, "destination": "", "protocols": ["http:80", "https:443"], "natural_key": "LAN_Z" + str(d + 4) + "U2_LAN_interne_usluge" + str(d + 4)}, {"labels": ["fw_rule"], "name": "Internet_Mail_server" + str(d + 4), "isactive": True, "fw_rule_mode": "allow", "source": "", "any_interface_incoming": False, "incoming_via_interface": "saiygvlo_vfqv_cdrw_vgaj_lnboivkiwlpv", "outgoing_via_interface": "", "any_interface_outgoing": False, "destination": id12, "protocols": ["https:443", "smtp:25", "imap:143", "pop3:110", "smtp_ssl:465", "imap_ssl:993", "pop3_ssl:995"], "natural_key": "Internet_Mail_server" + str(d + 4)}], "natural_key": "Firewall"}, {"labels": ["control", "aaa", "inherited_control"], "name": "AAA", "isactive": True, "mode": ["log"], "event_frequency": 10, "remotecredentialstore": id18, "localcredentialstore": "", "authorizations": [{"labels": ["authorization"], "name": "Domain admin", "user_account_id": "", "user_group_id": id20, "login_privilege": "admin", "natural_key": "Domain admin"}, {"labels": ["authorization"], "name": "Domain user", "user_account_id": "", "user_group_id": id19, "login_privilege": "user", "natural_key": "Domain user"}], "file_access_rules": [], "natural_key": "AAA", "authority": id21}]
        for l in (pc_id):
            if l in input2_data[k]["id"]:
                input2_data[k]["proxy_config"]["machine_id"] = id6
                input2_data[k]["controls"] = [{"labels": ["control", "aaa", "inherited_control"], "name": "AAA", "isactive": True, "mode": ["log"], "event_frequency": 10, "remotecredentialstore": id18, "localcredentialstore": "", "authorizations": [{"labels": ["authorization"], "name": "Domain admin", "user_account_id": "", "user_group_id": id20, "login_privilege": "admin", "natural_key": "Domain admin"}, {"labels": ["authorization"], "name": "Domain user", "user_account_id": "", "user_group_id": id19, "login_privilege": "user", "natural_key": "Domain user"}], "file_access_rules": [], "authority": id21}]
    startX += 2500
if av_to_turn_off != 0:
    for i in range(len(input2_data)):
        if "AV grupa Z" + str(av_to_turn_off) in input2_data[i]["name"]:
            input2_data[i]["members"] = [""]
            input2_data[i]["controls"] = []
input1.seek(0)
json.dump(input1_data, output1, indent=2)
json.dump(input2_data, output2, indent=2)