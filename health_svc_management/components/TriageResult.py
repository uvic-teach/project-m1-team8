class TriageResult:
    """
    Represents the result of a triage assessment for a patient.

    Attributes:
        _triage_id (int): The unique identifier for the triage assessment.
        _perform_date (str): The date the triage assessment was performed.
        _available_date (str): The date the triage assessment results are available.
        _patient_name (str): The name of the patient who was assessed.
        _summary (str): A summary of the triage assessment results.
        _detail (str): A detailed report of the triage assessment results.
        _suggestion (str): Suggestions for next steps based on the triage assessment results.
    """

    def __init__(self, triage_id: int, perform_date: str, available_date: str, patient_name: str, summary: str, detail: str, suggestion: str):
        """
        Initializes a new instance of the TriageResult class.

        Args:
            triage_id (int): The unique identifier for the triage assessment.
            perform_date (str): The date the triage assessment was performed.
            available_date (str): The date the triage assessment results are available.
            patient_name (str): The name of the patient who was assessed.
            summary (str): A summary of the triage assessment results.
            detail (str): A detailed report of the triage assessment results.
            suggestion (str): Suggestions for next steps based on the triage assessment results.
        """
        self._triage_id = triage_id
        self._perform_date = perform_date
        self._available_date = available_date
        self._patient_name = patient_name
        self._summary = summary
        self._detail = detail
        self._suggestion = suggestion

    @property
    def triage_id(self) -> int:
        """
        Gets the unique identifier for the triage assessment.

        Returns:
            int: The unique identifier for the triage assessment.
        """
        return self._triage_id

    @property
    def perform_date(self) -> str:
        """
        Gets the date the triage assessment was performed.

        Returns:
            str: The date the triage assessment was performed.
        """
        return self._perform_date

    @property
    def available_date(self) -> str:
        """
        Gets the date the triage assessment results are available.

        Returns:
            str: The date the triage assessment results are available.
        """
        return self._available_date

    @property
    def patient_name(self) -> str:
        """
        Gets the name of the patient who was assessed.

        Returns:
            str: The name of the patient who was assessed.
        """
        return self._patient_name

    @property
    def summary(self) -> str:
        """
        Gets a summary of the triage assessment results.

        Returns:
            str: A summary of the triage assessment results.
        """
        return self._summary

    @property
    def detail(self) -> str:
        """
        Gets a detailed report of the triage assessment results.

        Returns:
            str: A detailed report of the triage assessment results.
        """
        return self._detail

    @property
    def suggestion(self) -> str:
        """
        Gets suggestions for next steps based on the triage assessment results.

        Returns:
            str: Suggestions for next steps based on the triage assessment results.
        """
        return self._suggestion

    def sendNotificationResult(self, notificationSvc: NotificationSvc):
        """
        Sends a notification to the patient with the triage assessment results.

        Args:
            notificationSvc (NotificationSvc): The notification service to use to send the notification.
        """
        notificationSvc.sendNotification(self._triage_id, self._patient_name, self._available_date)
