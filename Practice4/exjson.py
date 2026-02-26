import json

with open("/home/iroumen/Documents/well/lol/Practice4/sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 75)
print("DN".ljust(55), "Speed".ljust(10), "MTU")
print("-" * 75)

for item in data["imdata"]:
    a = item["l1PhysIf"]["attributes"]
    dn = a["dn"]
    speed = a["speed"]
    mtu = a["mtu"]

    print(dn.ljust(55), speed.ljust(10), mtu)