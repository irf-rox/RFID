# 🚗 Moving Vehicle Details Detection using RFID

A practical and scalable system to detect and track moving vehicles using **RFID (Radio-Frequency Identification)** technology — designed with real-world deployment in mind and aligned with government regulations mandating in-built RFID tags in newly manufactured vehicles.

---

## 📄 Abstract

The **Moving Vehicle Detection System using RFID** is an intelligent system that enables the detection and tracking of moving vehicles through RFID tags. Each vehicle is affixed with a passive RFID tag (as per recent government schemes and GOEs), which emits a unique ID when it comes into the range of an RFID reader.

This project implements a cost-effective prototype of such a system, showcasing how data from RFID tags can be collected using basic RFID readers (which require no antennas or onboard power source), and how this data can be processed to identify the vehicle, including license plate association, timestamps, and potential location tagging.

🧠 This approach is inspired by and is an optimization of existing RFID-based applications such as:

* FASTag toll collection
* RFID-based student/staff attendance
* Retail anti-theft systems (RFID on clothes/items)

The project offers potential applications in **traffic monitoring**, **smart parking**, and **logistics tracking** by providing **real-time**, **reliable**, and **automated** vehicle detection.

---

## 🏆 Key Benefits

* 🔁 **Continuous Vehicle Monitoring**: Detects vehicles as they pass checkpoints.
* 📶 **Passive RFID Technology**: Low-cost, no onboard power required in tags.
* 🕒 **Real-Time Data Capture**: Logs vehicle presence instantly on detection.
* 📄 **Accurate Identification**: Each tag has a globally unique identifier (UID).
* 🔌 **Low Power Consumption**: Ideal for scalable deployments.
* ⚖️ **Government Policy Compliant**: Aligns with India’s push for mandatory RFID tagging in vehicles.

---

## 🔧 Hardware Requirements

* Arduino Uno/Nano/Mega
* RFID Reader Module (e.g., MFRC522)
* RFID Passive Tags (stickers or key fobs)
* Jumper wires
* Breadboard (optional)
* USB cable for programming

---

## 💻 Software Requirements

* [Arduino IDE](https://www.arduino.cc/en/software)
* MFRC522 Library (for interfacing with the RFID module)

To install MFRC522:

1. Open Arduino IDE
2. Go to `Sketch` → `Include Library` → `Manage Libraries`
3. Search for `MFRC522` and install it

---

## ⚙️ How It Works

1. An RFID tag is attached to each vehicle.
2. When a vehicle comes within range of the RFID reader, the tag transmits its UID.
3. The RFID reader captures the UID and sends it to the Arduino.
4. The Arduino processes this data and can display or log the UID for further analysis (e.g., match with license plate number or database records).

This system can be placed at:

* 🚦 Traffic checkpoints
* 🅿️ Parking lots
* 📦 Logistic gates
* 🏢 Campus entrances

---

## 🚀 Setup Instructions

1. **Clone this repository**

   ```bash
   git clone https://github.com/irf-rox/Moving-Vehicle-Details-Detection-using-RFID.git
   cd Moving-Vehicle-Details-Detection-using-RFID
   ```

2. **Connect the hardware**

   * Connect the RFID reader to Arduino as per the pin configuration in the code comments.
   * Power the board via USB or external source.

3. **Upload the sketch**

   * Open the `rfid_write_data.ino` file in Arduino IDE
   * Choose the correct board and COM port
   * Upload the code
   * Type in vehicle details and scan the RFID card to store them.

4. **Test the system**

   * Bring a registered RFID tag near the reader
   * The UID will appear on the serial monitor

---

## 📁 Project Structure

```
Moving-Vehicle-Details-Detection-using-RFID/
├── RFID_Vehicle_Detector.ino   # Main Arduino sketch
├── README.md                   # This documentation
└── rfid.py                     # License info
```

---

## 🌍 Real-World Applications

* **Smart Toll Collection** (like FASTag but broader)
* **Automated Parking Systems**
* **Vehicle Access Control for Secure Zones**
* **Campus Transport Monitoring**
* **Fleet Management & Logistics**

---

## 📈 Future Scope

* Integrate with **cloud-based vehicle databases**
* Enable **GPS+RFID hybrid tracking**
* Add **real-time dashboards** for traffic visualization
* Link RFID UID to vehicle number, driver identity, and violation history
* Provide push notifications for scanned vehicles.

---

## 🧑‍💻 Contribution

Want to improve the system or integrate it into your smart city project? Feel free to fork and submit a pull request! Contributions are welcome.

---

