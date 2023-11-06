from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship

from db import Base

class Medicine(Base):
    __tablename__ = "medicine"

    med_id = Column(Integer, primary_key=True,index=True)
    med_name = Column(String(200), nullable=False, index=True)
    main_purpose = Column(String(200), nullable=False)
    side_effect = Column(String(200), nullable=False)
    usage = Column(String(200), nullable=False)
    is_required_prescription = Column(Boolean, nullable=False)
    company = Column(String(200), nullable=False)
    usingredientsage = Column(String(200), nullable=False)

    def __repr__(self):
        return f'Medicine(med_id={self.med_id}, med_name={self.med_name}, main_purpose={self.main_purpose}, side_effect={self.side_effect}, usage={self.usage}, is_required_prescription={self.is_required_prescription}, company={self.company}, ingredients={self.ingredients})'
