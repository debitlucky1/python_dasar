hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("libur!")
    case "senin":
        print("semangat!")
    case _:
        print("hari kerja")