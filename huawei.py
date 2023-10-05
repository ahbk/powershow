from fusion_solar_py import client

ps = client.FusionSolarClient(
        username="username",
        password="password",
        huawei_subdomain="region03eu5")

stats = ps.get_power_status()

print(f"Current power: {stats.current_power_kw} kW")
print(f"Total power today: {stats.total_power_today_kwh} kWh")
print(f"Total power: {stats.total_power_kwh} kWh")

# log out - just in case
ps.log_out()
