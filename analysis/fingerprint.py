def fingerprint_device(bssid, rssi_history):
    if not rssi_history:
        return "unknown"

    avg_rssi = sum(rssi_history) / len(rssi_history)

    variance = sum((x - avg_rssi) ** 2 for x in rssi_history) / len(rssi_history)

    if variance > 100:
        return "unstable_signal"
    else:
        return "stable"