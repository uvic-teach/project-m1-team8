class Nurse:
    """
    Represents a nurse with their information.

    Attributes:
        nurse_id (int): The ID of the nurse.
        name (str): The name of the nurse.
        province (str): The province where the nurse is located.
        contact (str): The contact information of the nurse.
        address (str): The address of the nurse.
    """
    def __init__(self, nurse_id: int, name: str, province: str, contact: str, address: str) -> None:
        """
        Initializes a Nurse object with the given information.

        Args:
            nurse_id (int): The ID of the nurse.
            name (str): The name of the nurse.
            province (str): The province where the nurse is located.
            contact (str): The contact information of the nurse.
            address (str): The address of the nurse.
        """
        self.nurse_id = nurse_id
        self.name = name
        self.province = province
        self.contact = contact
        self.address = address
    
    def get_nurse_id(self) -> int:
        """
        Returns the ID of the nurse.

        Returns:
            int: The ID of the nurse.
        """
        return self.nurse_id
    
    def get_name(self) -> str:
        """
        Returns the name of the nurse.

        Returns:
            str: The name of the nurse.
        """
        return self.name
    
    def get_province(self) -> str:
        """
        Returns the province where the nurse is located.

        Returns:
            str: The province where the nurse is located.
        """
        return self.province
    
    def get_contact(self) -> str:
        """
        Returns the contact information of the nurse.

        Returns:
            str: The contact information of the nurse.
        """
        return self.contact
    
    def get_address(self) -> str:
        """
        Returns the address of the nurse.

        Returns:
            str: The address of the nurse.
        """
        return self.address
