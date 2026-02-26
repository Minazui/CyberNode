def evaluate_risk(scan):
    risk = 0

    if scan.rssi and scan.rssi > -30:
        risk += 2  # señal demasiado fuerte (posible proximidad sospechosa)

    if scan.ssid == "":
        risk += 1  # red oculta

    if scan.channel and scan.channel > 11:
        risk += 1  # canal poco común en algunas regiones

    if risk == 0:
        return "low"
    elif risk <= 2:
        return "medium"
    else:
        return "high"