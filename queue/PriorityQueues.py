from queue import PriorityQueue

class EmergencyRoom:
    def __init__(self):
        self.pq = PriorityQueue()
        self.count = 0  # tie-breaker for same priority

    def add_patient(self, name, severity):
        """
        Add patient to queue.
        Severity: lower number = more urgent
        """
        self.pq.put((name, self.count, severity))
        self.count += 1
        print(f"Added patient: {name} (severity={severity})")

    def treat_patient(self):
        """Treat the patient with highest priority (lowest severity)."""
        if self.pq.empty():
            print("No patients waiting.")
            return
        name,severity, count = self.pq.get()
        print(f"(severity={severity}) Treated patient: {name} " ,"count:",count)


# --- Demo ---
er = EmergencyRoom()
er.add_patient("John", 3)
er.add_patient("Amit", 2)
er.add_patient("Rohan", 1)
er.add_patient("SameSeverity1", 2)

# Treat patients
er.treat_patient()  # Rohan (severity 1)
er.treat_patient()  # Amit (severity 2)
er.treat_patient()  # SameSeverity1 (severity 2)
er.treat_patient()  # John (severity 3)
