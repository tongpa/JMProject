# -*- coding: utf-8 -*-
import os
from datetime import datetime
from hashlib import sha256
__all__ = ['DayConfig','SysMUser']
 
from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, Index, Integer, Numeric, SmallInteger, String, Text, Time, VARBINARY, text
from sqlalchemy.types import Unicode, Integer, DateTime,BigInteger
from sqlalchemy.orm import relation, synonym,mapper,relationship
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.ext.automap import automap_base

from exportemaildata.model import DeclarativeBase2, metadata2, DBSession2 
 




class BatTEmail(DeclarativeBase2):
    __tablename__ = 'bat_t_email'

    ID_EMAIL = Column(BigInteger, primary_key=True)
    RECEIVE = Column(String(255), nullable=False)
    SUBJECT = Column(String(255), nullable=False)
    EMAIL_ID = Column(BigInteger, nullable=False)
    PARAMETER = Column(String(512))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class FumMFormula(DeclarativeBase2):
    __tablename__ = 'fum_m_formula'

    ID_FORMULA = Column(BigInteger, primary_key=True)
    FORMULA_TYPE = Column(String(50))
    FORMULA_NAME = Column(String(255))
    FORMULA = Column(String(255))
    OUT = Column(String(255))
    UNIT = Column(String(255))
    OUT_TYPE = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class FumMFormulaEffect(DeclarativeBase2):
    __tablename__ = 'fum_m_formula_effect'

    ID_FORMULA = Column(ForeignKey(u'fum_m_formula.ID_FORMULA'), primary_key=True, nullable=False)
    SEQ = Column(Integer, primary_key=True, nullable=False)
    SYMBOL = Column(ForeignKey(u'fum_m_symbol.SYMBOL'), primary_key=True, nullable=False, index=True)
    ID_FORMULA_INPUT = Column(ForeignKey(u'fum_m_formula.ID_FORMULA'), index=True)
    NUMBER_TEXT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    fum_m_formula = relationship(u'FumMFormula', primaryjoin='FumMFormulaEffect.ID_FORMULA == FumMFormula.ID_FORMULA')
    fum_m_formula1 = relationship(u'FumMFormula', primaryjoin='FumMFormulaEffect.ID_FORMULA_INPUT == FumMFormula.ID_FORMULA')
    fum_m_symbol = relationship(u'FumMSymbol')


class FumMSymbol(DeclarativeBase2):
    __tablename__ = 'fum_m_symbol'

    SYMBOL = Column(String(20), primary_key=True)
    SYMBOL_TYPE = Column(String(20))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPcEcAddres(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pc_ec_address'

    ID_AP_PC_EC_ADDRESS = Column(BigInteger, primary_key=True)
    HOUSING_NO = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE = Column(String(255))
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    TEL_PREFIX_NO = Column(String(255))
    TEL_NO = Column(String(255))
    TEL_EXT_NO = Column(String(255))
    MOBILE_PREFIX_NO = Column(String(255))
    MOBILE_NO = Column(String(255))
    FAX_PREFIX_NO = Column(String(255))
    FAX_NO = Column(String(255))
    FAX_EXT_NO = Column(String(255))
    ID_GPS_TYPE = Column(ForeignKey(u'job_n_gps_type.ID_GPS_TYPE'), index=True)
    LAT = Column(String(255))
    LNG = Column(String(255))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_gps_type = relationship(u'JobNGpsType')
    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_n_province = relationship(u'JobNProvince')


class JobAApPcEcAddressLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pc_ec_address_lang'

    ID_AP_PC_EC_ADDRESS_LANG = Column(BigInteger, primary_key=True)
    ID_AP_PC_EC_ADDRESS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPcEmergencyContactLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pc_emergency_contact_lang'

    ID_AP_PC_EMERGENCY_CONTACT_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    WORK_POSITON = Column(String(255))
    RELATIONSHIP = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPersonalSkill(DeclarativeBase2):
    __tablename__ = 'job_a_ap_personal_skill'

    ID_AP_PERSONAL_SKILL = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    SEQ = Column(SmallInteger)
    ID_PERSONAL_SKILL_GROUP = Column(ForeignKey(u'job_n_personal_skill_group.ID_PERSONAL_SKILL_GROUP'), index=True)
    SCORE_PERSONAL_SKILL_GROUP = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_personal_skill_group = relationship(u'JobNPersonalSkillGroup')


class JobAApPiFbRelationship(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pi_fb_relationship'

    ID_AP_PI_FB_RELATIONSHIP = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_APPLICANT_FAMILY = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_APPLICANT_FAMILY_TYPE = Column(ForeignKey(u'job_n_applicant_family_type.ID_APPLICANT_FAMILY_TYPE'), index=True)
    IS_ALIVE = Column(String(1))
    DATE_DEAD = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    ID_DISEASES = Column(ForeignKey(u'job_n_diseases.ID_DISEASES'), index=True)
    CHOICE_LIVING_CONDITION = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant', primaryjoin='JobAApPiFbRelationship.ID_APPLICANT == JobAApplicant.ID_APPLICANT')
    job_a_applicant1 = relationship(u'JobAApplicant', primaryjoin='JobAApPiFbRelationship.ID_APPLICANT_FAMILY == JobAApplicant.ID_APPLICANT')
    job_n_applicant_family_type = relationship(u'JobNApplicantFamilyType')
    job_n_disease = relationship(u'JobNDisease')


class JobAApPiHobbieActivitie(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pi_hobbie_activitie'

    ID_AP_PI_HOBBIE_ACTIVITIE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_HOBBIE_TYPE = Column(ForeignKey(u'job_n_hobbie_type.ID_HOBBIE_TYPE'), index=True)
    ID_HOBBIE = Column(ForeignKey(u'job_n_hobbie.ID_HOBBIE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_hobbie = relationship(u'JobNHobbie')
    job_n_hobbie_type = relationship(u'JobNHobbieType')


class JobAApPiIdVehicle(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pi_id_vehicle'

    ID_AP_PI_ID_VEHICLE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_VEHICLE = Column(ForeignKey(u'job_n_vehicle.ID_VEHICLE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_vehicle = relationship(u'JobNVehicle')


class JobAApPiPastRecord(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pi_past_record'

    ID_AP_PI_PAST_RECORD = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_PERSONAL_PAST_RECORD_ANSWER = Column(ForeignKey(u'job_n_personal_past_record_answer.ID_PERSONAL_PAST_RECORD_ANSWER'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_personal_past_record_answer = relationship(u'JobNPersonalPastRecordAnswer')


class JobAApPiPersonalDataLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pi_personal_data_lang'

    ID_AP_PI_PERSONAL_DATA_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    SCAR = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPiPersonalStatusLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pi_personal_status_lang'

    ID_AP_PI_PERSONAL_STATUS_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    TAMPLE_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPqEdEdInternshipExperience(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ed_ed_internship_experience'

    ID_AP_PQ_ED_ED_INTERNSHIP_EXPERIENCE = Column(BigInteger, primary_key=True)
    ID_AP_PQ_ED_EDUCATION = Column(ForeignKey(u'job_a_ap_pq_ed_education.ID_AP_PQ_ED_EDUCATION'), index=True)
    DATE_FROM = Column(Date)
    DATE_TO = Column(Date)
    ID_APPLICANT_COMPANY = Column(ForeignKey(u'job_a_applicant_company.ID_APPLICANT_COMPANY'), index=True)
    ID_PREFIX_NAME_BOSS = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    BOSS_FIRST_NAME = Column(String(255))
    BOSS_MID_NAME = Column(String(255))
    BOSS_LAST_NAME = Column(String(255))
    BOSS_MAIDEN_NAME = Column(String(255))
    BOSS_NICK_NAME = Column(String(255))
    BOSS_POSITION = Column(String(255))
    BOSS_SCOPE_OF_WORK = Column(Text)
    DESCRIBE_COMPANY = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant_company = relationship(u'JobAApplicantCompany')
    job_a_ap_pq_ed_education = relationship(u'JobAApPqEdEducation')
    job_n_prefix_name = relationship(u'JobNPrefixName')


class JobAApPqEdEdInternshipExperienceLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ed_ed_internship_experience_lang'

    ID_AP_PQ_ED_ED_INTERNSHIP_EXPERIENCE_LANG = Column(BigInteger, primary_key=True)
    ID_AP_PQ_ED_ED_INTERNSHIP_EXPERIENCE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    BOSS_FIRST_NAME = Column(String(255))
    BOSS_MID_NAME = Column(String(255))
    BOSS_LAST_NAME = Column(String(255))
    BOSS_MAIDEN_NAME = Column(String(255))
    BOSS_NICK_NAME = Column(String(255))
    BOSS_POSITION = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPqEdEdTraining(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ed_ed_training'

    ID_AP_PQ_ED_ED_TRAINING = Column(BigInteger, primary_key=True)
    ID_AP_PQ_ED_EDUCATION = Column(ForeignKey(u'job_a_ap_pq_ed_education.ID_AP_PQ_ED_EDUCATION'), index=True)
    TRAINING_YEAR = Column(Integer)
    COURSE_NAME = Column(String(255))
    INSTITUTION = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    DURATION_YEAR = Column(Integer)
    DURATION_MONTH = Column(Integer)
    DURATION_DAY = Column(Integer)
    BENEFIT = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_ap_pq_ed_education = relationship(u'JobAApPqEdEducation')
    job_n_country = relationship(u'JobNCountry')


class JobAApPqEdEdTrainingLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ed_ed_training_lang'

    ID_AP_PQ_ED_ED_TRAINING_LANG = Column(BigInteger, primary_key=True)
    ID_AP_PQ_ED_ED_TRAINING = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    COURSE_NAME = Column(String(255))
    INSTITUTION = Column(String(255))
    BENEFIT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPqEdEducation(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ed_education'

    ID_AP_PQ_ED_EDUCATION = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    CHOICE_CURRENTLY = Column(String(1))
    GRADUATED_SINCE = Column(Date)
    STUDY_ON_YEAR = Column(Integer)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ID_EDUCATION_LEVEL = Column(ForeignKey(u'job_n_education_level.ID_EDUCATION_LEVEL'), index=True)
    ID_DEGREE = Column(ForeignKey(u'job_n_degree.ID_DEGREE'), index=True)
    ID_UNIVERSITY = Column(ForeignKey(u'job_n_university.ID_UNIVERSITY'), index=True)
    ID_FACULTY = Column(ForeignKey(u'job_n_faculty.ID_FACULTY'), index=True)
    ID_FIELD_STUDY = Column(ForeignKey(u'job_n_field_study.ID_FIELD_STUDY'), index=True)
    ID_MAJOR = Column(ForeignKey(u'job_n_major.ID_MAJOR'), index=True)
    PERIOD_FROM = Column(Integer)
    PERIOD_TO = Column(Integer)
    GRADUATED_YEAR = Column(Integer)
    GPA = Column(Numeric(5, 2))
    ID_HONOR = Column(ForeignKey(u'job_n_honor.ID_HONOR'), index=True)
    EXTRA_CURRICULAR_ACTIVITIES = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_degree = relationship(u'JobNDegree')
    job_n_education_level = relationship(u'JobNEducationLevel')
    job_n_faculty = relationship(u'JobNFaculty')
    job_n_field_study = relationship(u'JobNFieldStudy')
    job_n_honor = relationship(u'JobNHonor')
    job_n_major = relationship(u'JobNMajor')
    job_n_province = relationship(u'JobNProvince')
    job_n_university = relationship(u'JobNUniversity')


class JobAApPqPsDrivingSkillLicense(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_driving_skill_license'

    ID_AP_PQ_PS_DRIVING_SKILL_LICENSE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_VEHICLE = Column(ForeignKey(u'job_n_vehicle.ID_VEHICLE'), index=True)
    IS_HAVE_LICENSE = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_vehicle = relationship(u'JobNVehicle')


class JobAApPqPsDsDrivingLicense(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_ds_driving_license'

    ID_AP_PQ_PS_DS_DRIVING_LICENSE = Column(BigInteger, primary_key=True)
    ID_AP_PQ_PS_DRIVING_SKILL_LICENSE = Column(ForeignKey(u'job_a_ap_pq_ps_driving_skill_license.ID_AP_PQ_PS_DRIVING_SKILL_LICENSE'), index=True)
    LICENSE_NO = Column(String(255))
    ID_VEHICLE_CLASS = Column(ForeignKey(u'job_n_vehicle_class.ID_VEHICLE_CLASS'), index=True)
    ISSUED_BY = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    DATE_ISSUED = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_ap_pq_ps_driving_skill_license = relationship(u'JobAApPqPsDrivingSkillLicense')
    job_n_country = relationship(u'JobNCountry')
    job_n_province = relationship(u'JobNProvince')
    job_n_vehicle_clas = relationship(u'JobNVehicleClas')


class JobAApPqPsLanguageProficiency(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_language_proficiency'

    ID_AP_PQ_PS_LANGUAGE_PROFICIENCY = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    ID_EVALUATION_LANGUAGE_SPEAKING = Column(ForeignKey(u'job_n_evaluation_language.ID_EVALUATION_LANGUAGE'), index=True)
    ID_EVALUATION_LANGUAGE_READING = Column(ForeignKey(u'job_n_evaluation_language.ID_EVALUATION_LANGUAGE'), index=True)
    ID_EVALUATION_LANGUAGE_LISTENING = Column(ForeignKey(u'job_n_evaluation_language.ID_EVALUATION_LANGUAGE'), index=True)
    ID_EVALUATION_LANGUAGE_WRITING = Column(ForeignKey(u'job_n_evaluation_language.ID_EVALUATION_LANGUAGE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_evaluation_language = relationship(u'JobNEvaluationLanguage', primaryjoin='JobAApPqPsLanguageProficiency.ID_EVALUATION_LANGUAGE_LISTENING == JobNEvaluationLanguage.ID_EVALUATION_LANGUAGE')
    job_n_evaluation_language1 = relationship(u'JobNEvaluationLanguage', primaryjoin='JobAApPqPsLanguageProficiency.ID_EVALUATION_LANGUAGE_READING == JobNEvaluationLanguage.ID_EVALUATION_LANGUAGE')
    job_n_evaluation_language2 = relationship(u'JobNEvaluationLanguage', primaryjoin='JobAApPqPsLanguageProficiency.ID_EVALUATION_LANGUAGE_SPEAKING == JobNEvaluationLanguage.ID_EVALUATION_LANGUAGE')
    job_n_evaluation_language3 = relationship(u'JobNEvaluationLanguage', primaryjoin='JobAApPqPsLanguageProficiency.ID_EVALUATION_LANGUAGE_WRITING == JobNEvaluationLanguage.ID_EVALUATION_LANGUAGE')
    job_n_language = relationship(u'JobNLanguage')


class JobAApPqPsLanguageScoreTest(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_language_score_test'

    ID_AP_PQ_PS_LANGUAGE_SCORE_TEST = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    ID_LANGUAGE_STANDARDIZED_TEST = Column(ForeignKey(u'job_n_language_standardized_test.ID_LANGUAGE_STANDARDIZED_TEST'), index=True)
    ID_LANGUAGE_STANDARDIZED_TEST_LEVEL = Column(ForeignKey(u'job_n_language_standardized_test_level.ID_LANGUAGE_STANDARDIZED_TEST_LEVEL'), index=True)
    SCORE_SPEAKING = Column(Integer)
    SCORE_READING = Column(Integer)
    SCORE_LISTENING = Column(Integer)
    SCORE_WRITING = Column(Integer)
    SCORE_TOTAL = Column(Integer)
    DATE_ISSUED = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_language = relationship(u'JobNLanguage')
    job_n_language_standardized_test = relationship(u'JobNLanguageStandardizedTest')
    job_n_language_standardized_test_level = relationship(u'JobNLanguageStandardizedTestLevel')


class JobAApPqPsOfficeMachineSkill(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_office_machine_skill'

    ID_AP_PQ_PS_OFFICE_MACHINE_SKILL = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_OFFICE_MACHINE_SKILL = Column(ForeignKey(u'job_n_office_machine_skill.ID_OFFICE_MACHINE_SKILL'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_office_machine_skill = relationship(u'JobNOfficeMachineSkill')


class JobAApPqPsProfessionalLicense(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_professional_license'

    ID_AP_PQ_PS_PROFESSIONAL_LICENSE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_PROFESSIONAL_LICENSE = Column(ForeignKey(u'job_n_professional_license.ID_PROFESSIONAL_LICENSE'), index=True)
    LICENSE_NO = Column(String(255))
    ISSUED_BY = Column(String(255))
    DATE_ISSUED = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_professional_license = relationship(u'JobNProfessionalLicense')


class JobAApPqPsSpecialSkill(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_special_skill'

    ID_AP_PQ_PS_SPECIAL_SKILL = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_JOB_SPECIAL_SKILL = Column(BigInteger, index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_job_division = relationship(u'JobNJobDivision')


class JobAApPqPsSpecialSkillComputer(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_special_skill_computer'

    ID_AP_PQ_PS_SPECIAL_SKILL_COMPUTER = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_SPECIAL_SKILL_COMPUTER_TYPE = Column(ForeignKey(u'job_n_special_skill_computer_type.ID_SPECIAL_SKILL_COMPUTER_TYPE'), index=True)
    ID_SPECIAL_SKILL_COMPUTER = Column(ForeignKey(u'job_n_special_skill_computer.ID_SPECIAL_SKILL_COMPUTER'), index=True)
    ID_PROFICIENCY_SKILL_COMPUTER = Column(ForeignKey(u'job_n_proficiency_skill_computer.ID_PROFICIENCY_SKILL_COMPUTER'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_proficiency_skill_computer = relationship(u'JobNProficiencySkillComputer')
    job_n_special_skill_computer = relationship(u'JobNSpecialSkillComputer')
    job_n_special_skill_computer_type = relationship(u'JobNSpecialSkillComputerType')


class JobAApPqPsTypingSkill(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_typing_skill'

    ID_AP_PQ_PS_TYPING_SKILL = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    WORD_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_language = relationship(u'JobNLanguage')


class JobAApPqPsVehicle(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_ps_vehicle'

    ID_AP_PQ_PS_VEHICLE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_VEHICLE = Column(ForeignKey(u'job_n_vehicle.ID_VEHICLE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_vehicle = relationship(u'JobNVehicle')


class JobAApPqWeWeFringeBenefit(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_fringe_benefit'

    ID_AP_PQ_WE_WE_FRINGE_BENEFIT = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WORK_EXPERIENCE = Column(ForeignKey(u'job_a_ap_pq_we_work_experience.ID_AP_PQ_WE_WORK_EXPERIENCE'), index=True)
    ID_FRINGE_BENEFIT = Column(ForeignKey(u'job_n_fringe_benefit.ID_FRINGE_BENEFIT'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_ap_pq_we_work_experience = relationship(u'JobAApPqWeWorkExperience')
    job_n_fringe_benefit = relationship(u'JobNFringeBenefit')


class JobAApPqWeWeIncomeTax(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_income_tax'

    ID_AP_PQ_WE_WE_INCOME_TAX = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WORK_EXPERIENCE = Column(ForeignKey(u'job_a_ap_pq_we_work_experience.ID_AP_PQ_WE_WORK_EXPERIENCE'), index=True)
    ID_INCOME_TAX_PAYMENT = Column(ForeignKey(u'job_n_income_tax_payment.ID_INCOME_TAX_PAYMENT'), index=True)
    AMOUNT = Column(Numeric(20, 2))
    ID_CURRENCY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_ap_pq_we_work_experience = relationship(u'JobAApPqWeWorkExperience')
    job_n_currency = relationship(u'JobNCurrency')
    job_n_income_tax_payment = relationship(u'JobNIncomeTaxPayment')


class JobAApPqWeWeTraining(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_training'

    ID_AP_PQ_WE_WE_TRAINING = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WORK_EXPERIENCE = Column(ForeignKey(u'job_a_ap_pq_we_work_experience.ID_AP_PQ_WE_WORK_EXPERIENCE'), index=True)
    TRAINING_YEAR = Column(Integer)
    COURSE_NAME = Column(String(255))
    INSTITUTION = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    DURATION_YEAR = Column(Integer)
    DURATION_MONTH = Column(Integer)
    DURATION_DAY = Column(Integer)
    BENEFIT = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_ap_pq_we_work_experience = relationship(u'JobAApPqWeWorkExperience')
    job_n_country = relationship(u'JobNCountry')


class JobAApPqWeWeTrainingLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_training_lang'

    ID_AP_PQ_WE_WE_TRAINING_LANG = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WE_TRAINING = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    COURSE_NAME = Column(VARBINARY(255))
    INSTITUTION = Column(String(255))
    BENEFIT = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPqWeWeWorkPosition(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_work_position'

    ID_AP_PQ_WE_WE_WORK_POSITION = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WORK_EXPERIENCE = Column(ForeignKey(u'job_a_ap_pq_we_work_experience.ID_AP_PQ_WE_WORK_EXPERIENCE'), index=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    POSITION_NAME = Column(String(255))
    ID_JOB_POSITION = Column(ForeignKey(u'job_n_job_position.ID_JOB_POSITION'), index=True)
    ID_CAREER = Column(ForeignKey(u'job_n_career.ID_CAREER'), index=True)
    CHOICE_CURRENT_WORKING = Column(String(1))
    DATE_PERIOD_FROM = Column(Date)
    DATE_PERIOD_TO = Column(Date)
    NO_OF_SUBORDINATE = Column(Integer)
    ID_CURRENCY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_a_ap_pq_we_work_experience = relationship(u'JobAApPqWeWorkExperience')
    job_n_career = relationship(u'JobNCareer')
    job_n_currency = relationship(u'JobNCurrency')
    job_n_job_position = relationship(u'JobNJobPosition')


class JobAApPqWeWeWorkPositionLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_work_position_lang'

    ID_AP_PQ_WE_WE_WORK_POSITION_LANG = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WE_WORK_POSITION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    POSITION_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPqWeWeWpIncomeBase(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_wp_income_base'

    ID_AP_PQ_WE_WE_WP_INCOME_BASE = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WE_WORK_POSITION = Column(ForeignKey(u'job_a_ap_pq_we_we_work_position.ID_AP_PQ_WE_WE_WORK_POSITION'), index=True)
    ID_SALARY_BASE = Column(ForeignKey(u'job_n_salary_base.ID_SALARY_BASE'), index=True)
    ID_SALARY_PER_AMOUNT = Column(ForeignKey(u'job_n_salary_per_amount.ID_SALARY_PER_AMOUNT'), index=True)
    AMOUNT = Column(Numeric(20, 2))
    AMONT_USD = Column(Numeric(20, 2))
    AMONT_USD_RATE = Column(Numeric(20, 6))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_ap_pq_we_we_work_position = relationship(u'JobAApPqWeWeWorkPosition')
    job_n_salary_base = relationship(u'JobNSalaryBase')
    job_n_salary_per_amount = relationship(u'JobNSalaryPerAmount')


class JobAApPqWeWeWpJobExperience(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_we_wp_job_experience'

    ID_AP_PQ_WE_WE_WP_JOB_EXPERIENCE = Column(BigInteger, primary_key=True)
    ID_AP_PQ_WE_WE_WORK_POSITION = Column(ForeignKey(u'job_a_ap_pq_we_we_work_position.ID_AP_PQ_WE_WE_WORK_POSITION'), index=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_APPLICANT_COMPANY = Column(ForeignKey(u'job_a_applicant_company.ID_APPLICANT_COMPANY'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_JOB_INDUSTRY = Column(ForeignKey(u'job_n_job_industry.ID_JOB_INDUSTRY'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    ID_JOB_EXPERIENCE = Column(ForeignKey(u'job_n_job_experience.ID_JOB_EXPERIENCE'), index=True)
    DATE_PERIOD_FROM = Column(Date)
    DATE_PERIOD_TO = Column(Date)
    TOTAL_YEAR = Column(Integer)
    TOTAL_MONTH = Column(Integer)
    TOTAL_DAY = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_a_applicant_company = relationship(u'JobAApplicantCompany')
    job_a_ap_pq_we_we_work_position = relationship(u'JobAApPqWeWeWorkPosition')
    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_experience = relationship(u'JobNJobExperience')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    job_n_job_industry = relationship(u'JobNJobIndustry')


class JobAApPqWeWorkExperience(DeclarativeBase2):
    __tablename__ = 'job_a_ap_pq_we_work_experience'

    ID_AP_PQ_WE_WORK_EXPERIENCE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    SEQ = Column(SmallInteger)
    ID_CURRENT_EMPLOYMENT_STATUS = Column(ForeignKey(u'job_n_current_employment_status.ID_CURRENT_EMPLOYMENT_STATUS'), index=True)
    ID_EMPLOYMENT_TYPE = Column(ForeignKey(u'job_n_employment_type.ID_EMPLOYMENT_TYPE'), index=True)
    DATE_PERIOD_FROM = Column(Date)
    DATE_PERIOD_TO = Column(Date)
    ID_DAY_WORKING_FROM = Column(ForeignKey(u'job_n_day.ID_DAY'), index=True)
    ID_DAY_WORKING_TO = Column(ForeignKey(u'job_n_day.ID_DAY'), index=True)
    WORKING_HOUR_FROM = Column(Time)
    WORKING_HOUR_TO = Column(Time)
    CHOICE_REASON_LEAVING = Column(String(1))
    ID_LEAVING_RESIGNATION = Column(ForeignKey(u'job_n_leaving_resignation.ID_LEAVING_RESIGNATION'), index=True)
    ID_LEAVING_DISMISSED = Column(ForeignKey(u'job_n_leaving_dismissed.ID_LEAVING_DISMISSED'), index=True)
    REASON = Column(Text)
    IS_TRAINING = Column(String(1))
    IS_INCOME_TAX = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    ID_DURING_UNEMPLOYED = Column(ForeignKey(u'job_n_during_unemployed.ID_DURING_UNEMPLOYED'), index=True)
    ID_ENTREPRENER_TYPE = Column(ForeignKey(u'job_n_entreprener_type.ID_ENTREPRENER_TYPE'), index=True)
    ID_APPLICANT_COMPANY = Column(ForeignKey(u'job_a_applicant_company.ID_APPLICANT_COMPANY'), index=True)
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_a_applicant_company = relationship(u'JobAApplicantCompany')
    job_n_current_employment_statu = relationship(u'JobNCurrentEmploymentStatu')
    job_n_day = relationship(u'JobNDay', primaryjoin='JobAApPqWeWorkExperience.ID_DAY_WORKING_FROM == JobNDay.ID_DAY')
    job_n_day1 = relationship(u'JobNDay', primaryjoin='JobAApPqWeWorkExperience.ID_DAY_WORKING_TO == JobNDay.ID_DAY')
    job_n_during_unemployed = relationship(u'JobNDuringUnemployed')
    job_n_employment_type = relationship(u'JobNEmploymentType')
    job_n_entreprener_type = relationship(u'JobNEntreprenerType')
    job_n_leaving_dismissed = relationship(u'JobNLeavingDismissed')
    job_n_leaving_resignation = relationship(u'JobNLeavingResignation')


class JobAApPsEvaluationPersonalSkill(DeclarativeBase2):
    __tablename__ = 'job_a_ap_ps_evaluation_personal_skill'

    ID_AP_PS_EVALUATION_PERSONAL_SKILL = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_AP_PERSONAL_SKILL = Column(ForeignKey(u'job_a_ap_personal_skill.ID_AP_PERSONAL_SKILL'), index=True)
    SEQ = Column(SmallInteger)
    ID_PERSONAL_SKILL_GROUP = Column(ForeignKey(u'job_n_personal_skill_group.ID_PERSONAL_SKILL_GROUP'), index=True)
    ID_PERSONAL_SKILL = Column(ForeignKey(u'job_n_personal_skill.ID_PERSONAL_SKILL'), index=True)
    ID_EVALUATION_PERSONAL_SKILL = Column(ForeignKey(u'job_n_evaluation_personal_skill.ID_EVALUATION_PERSONAL_SKILL'), index=True)
    SCORE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_a_ap_personal_skill = relationship(u'JobAApPersonalSkill')
    job_n_evaluation_personal_skill = relationship(u'JobNEvaluationPersonalSkill')
    job_n_personal_skill = relationship(u'JobNPersonalSkill')
    job_n_personal_skill_group = relationship(u'JobNPersonalSkillGroup')


class JobAApReferencePerson(DeclarativeBase2):
    __tablename__ = 'job_a_ap_reference_person'

    ID_AP_REFERENCE_PERSON = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    SEQ = Column(SmallInteger)
    ID_PREFIX_NAME = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    RELATIONSHIP = Column(String(255))
    ID_CAREER = Column(ForeignKey(u'job_n_career.ID_CAREER'), index=True)
    WORK_POSITION = Column(String(255))
    ID_APPLICANT_COMPANY = Column(ForeignKey(u'job_a_applicant_company.ID_APPLICANT_COMPANY'), index=True)
    TEL_PREFIX_NO = Column(String(255))
    TEL_NO = Column(String(255))
    TEL_EXT_NO = Column(String(255))
    MOBILE_PREFIX_NO = Column(String(255))
    MOBILE_NO = Column(String(255))
    FAX_PREFIX_NO = Column(String(255))
    FAX_NO = Column(String(255))
    FAX_EXT_NO = Column(String(255))
    EMAIL = Column(String(255))
    HOW_LONG_YEAR = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_a_applicant_company = relationship(u'JobAApplicantCompany')
    job_n_career = relationship(u'JobNCareer')
    job_n_prefix_name = relationship(u'JobNPrefixName')


class JobAApReferencePersonLang(DeclarativeBase2):
    __tablename__ = 'job_a_ap_reference_person_lang'

    ID_AP_REFERENCE_PERSON_LANG = Column(BigInteger, primary_key=True)
    ID_AP_REFERENCE_PERSON = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    RELATIONSHIP = Column(String(255))
    WORK_POSITION = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApplicant(DeclarativeBase2):
    __tablename__ = 'job_a_applicant'

    ID_APPLICANT = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    APPLICANT_OF_COUNTRY_NO = Column(String(255))
    DESCRIBE_YOURSELF = Column(Text)
    CHOICE_MANAGE_CRITERIA = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser')


class JobAApPcPostalAddres(JobAApplicant):
    __tablename__ = 'job_a_ap_pc_postal_address'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    ID_ADDRESS_PRESENT = Column(ForeignKey(u'job_m_user_address.ID_USER_ADDRESS'), index=True)
    CHOICE_HOUSE_REGISTRATION = Column(String(1))
    ID_ADDRESS_HOUSE_REGISTRATION = Column(ForeignKey(u'job_m_user_address.ID_USER_ADDRESS'), index=True)
    CHOICE_MAIL_ADDRESS = Column(String(1))
    ID_ADDRESS_MAIL = Column(ForeignKey(u'job_m_user_address.ID_USER_ADDRESS'), index=True)
    CHOICE_SHOW_MAP_RESUME = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_m_user_addres = relationship(u'JobMUserAddres', primaryjoin='JobAApPcPostalAddres.ID_ADDRESS_HOUSE_REGISTRATION == JobMUserAddres.ID_USER_ADDRESS')
    job_m_user_addres1 = relationship(u'JobMUserAddres', primaryjoin='JobAApPcPostalAddres.ID_ADDRESS_MAIL == JobMUserAddres.ID_USER_ADDRESS')
    job_m_user_addres2 = relationship(u'JobMUserAddres', primaryjoin='JobAApPcPostalAddres.ID_ADDRESS_PRESENT == JobMUserAddres.ID_USER_ADDRESS')


class JobAApPiFamilyBackground(JobAApplicant):
    __tablename__ = 'job_a_ap_pi_family_background'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    NO_FAMILY_SIZE = Column(Integer)
    CHOICE_PARENT_MARITAL_STATUS = Column(String(1))
    NO_OF_SIBLING = Column(Integer)
    NO_OF_SIBLING_BROTHER = Column(Integer)
    NO_OF_SIBLING_SISTER = Column(Integer)
    SIBLING_ARE_NO = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPersonalQualification(JobAApplicant):
    __tablename__ = 'job_a_ap_personal_qualification'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPersonalInfo(JobAApplicant):
    __tablename__ = 'job_a_ap_personal_info'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPcEmergencyContact(JobAApplicant):
    __tablename__ = 'job_a_ap_pc_emergency_contact'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    ID_AP_PC_EC_ADDRESS = Column(ForeignKey(u'job_a_ap_pc_ec_address.ID_AP_PC_EC_ADDRESS'), index=True)
    ID_PREFIX_NAME = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    ID_CAREER = Column(ForeignKey(u'job_n_career.ID_CAREER'), index=True)
    ID_APPLICANT_COMPANY = Column(ForeignKey(u'job_a_applicant_company.ID_APPLICANT_COMPANY'), index=True)
    WORK_POSITON = Column(String(255))
    EMAIL = Column(String(255))
    RELATIONSHIP = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant_company = relationship(u'JobAApplicantCompany')
    job_a_ap_pc_ec_addres = relationship(u'JobAApPcEcAddres')
    job_n_career = relationship(u'JobNCareer')
    job_n_prefix_name = relationship(u'JobNPrefixName')


class JobAApPqWorkExperience(JobAApplicant):
    __tablename__ = 'job_a_ap_pq_work_experience'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    EXPERIENCE_YEAR = Column(Integer)
    EXPERIENCE_MONTH = Column(Integer)
    EXPERIENCE_DAY = Column(Integer)
    EXPERIENCE_DAY_TOTAL = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPersonalContact(JobAApplicant):
    __tablename__ = 'job_a_ap_personal_contact'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPiPersonalStatu(JobAApplicant):
    __tablename__ = 'job_a_ap_pi_personal_status'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    ID_MILITARY_STATUS = Column(ForeignKey(u'job_n_military_status.ID_MILITARY_STATUS'), index=True)
    ID_MILITARY_EXEMPTED = Column(ForeignKey(u'job_n_military_exempted.ID_MILITARY_EXEMPTED'), index=True)
    DATE_MILITARY_DRAFT_IN = Column(Date)
    IS_ORDINATION = Column(String(1))
    TAMPLE_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_military_exempted = relationship(u'JobNMilitaryExempted')
    job_n_military_statu = relationship(u'JobNMilitaryStatu')


class JobAApPiPersonalDatum(JobAApplicant):
    __tablename__ = 'job_a_ap_pi_personal_data'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    ID_PREFIX_NAME = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    ID_PREFIX_NAME_LOCAL = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    FIRST_NAME_LOCAL = Column(String(255))
    MID_NAME_LOCAL = Column(String(255))
    LAST_NAME_LOCAL = Column(String(255))
    MAIDEN_NAME_LOCAL = Column(String(255))
    NICK_NAME_LOCAL = Column(String(255))
    DATE_BIRTH = Column(Date)
    ID_COUNTRY_BIRTH = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE_BIRTH = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY_BIRTH = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_GENDER = Column(ForeignKey(u'job_n_gender.ID_GENDER'), index=True)
    ID_EYE_COLOR = Column(ForeignKey(u'job_n_eye_color.ID_EYE_COLOR'), index=True)
    ID_COMPLEXION = Column(ForeignKey(u'job_n_complexion.ID_COMPLEXION'), index=True)
    SCAR = Column(String(255))
    WEIGHT = Column(Numeric(10, 2))
    WEIGHT_G = Column(Numeric(10, 2))
    ID_WEIGHT_UNIT = Column(ForeignKey(u'job_n_weight_unit.ID_WEIGHT_UNIT'), index=True)
    HEIGHT = Column(Numeric(10, 2))
    HEIGHT_CM = Column(Numeric(10, 2))
    ID_HEIGHT_UNIT = Column(ForeignKey(u'job_n_height_unit.ID_HEIGHT_UNIT'), index=True)
    ID_BLOOD_GROUP = Column(ForeignKey(u'job_n_blood_group.ID_BLOOD_GROUP'), index=True)
    IS_HANDICAPPED = Column(String(1))
    HANDICAPPED_NO = Column(String(255))
    ID_HANDICAPPED_TYPE = Column(ForeignKey(u'job_n_handicapped_type.ID_HANDICAPPED_TYPE'), index=True)
    CHOICE_HANDICAPPED_RESTORATION = Column(String(1))
    ID_NATIONALITY_BIRTH = Column(ForeignKey(u'job_n_nationality.ID_NATIONALITY'), index=True)
    ID_NATIONALITY_PRESENT = Column(ForeignKey(u'job_n_nationality.ID_NATIONALITY'), index=True)
    ID_RACE = Column(ForeignKey(u'job_n_race.ID_RACE'), index=True)
    ID_RELIGION = Column(ForeignKey(u'job_n_religion.ID_RELIGION'), index=True)
    ID_MARITAL_STATUS = Column(ForeignKey(u'job_n_marital_status.ID_MARITAL_STATUS'), index=True)
    CHOISE_MARITAL_TYPE = Column(String(1))
    IS_CHILD = Column(String(1))
    NO_CHILD_SON = Column(Integer)
    NO_CHILD_DAUGHTER = Column(Integer)
    IS_ADOPT_CHILD = Column(String(1))
    NO_ADOPT_CHILD_SON = Column(Integer)
    NO_ADOPT_CHILD_DAUGHTER = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_blood_group = relationship(u'JobNBloodGroup')
    job_n_city = relationship(u'JobNCity')
    job_n_complexion = relationship(u'JobNComplexion')
    job_n_country = relationship(u'JobNCountry')
    job_n_eye_color = relationship(u'JobNEyeColor')
    job_n_gender = relationship(u'JobNGender')
    job_n_handicapped_type = relationship(u'JobNHandicappedType')
    job_n_height_unit = relationship(u'JobNHeightUnit')
    job_n_marital_statu = relationship(u'JobNMaritalStatu')
    job_n_nationality = relationship(u'JobNNationality', primaryjoin='JobAApPiPersonalDatum.ID_NATIONALITY_BIRTH == JobNNationality.ID_NATIONALITY')
    job_n_nationality1 = relationship(u'JobNNationality', primaryjoin='JobAApPiPersonalDatum.ID_NATIONALITY_PRESENT == JobNNationality.ID_NATIONALITY')
    job_n_prefix_name = relationship(u'JobNPrefixName', primaryjoin='JobAApPiPersonalDatum.ID_PREFIX_NAME == JobNPrefixName.ID_PREFIX_NAME')
    job_n_prefix_name1 = relationship(u'JobNPrefixName', primaryjoin='JobAApPiPersonalDatum.ID_PREFIX_NAME_LOCAL == JobNPrefixName.ID_PREFIX_NAME')
    job_n_province = relationship(u'JobNProvince')
    job_n_race = relationship(u'JobNRace')
    job_n_religion = relationship(u'JobNReligion')
    job_n_weight_unit = relationship(u'JobNWeightUnit')


class JobAApPqEducationNotgen(JobAApplicant):
    __tablename__ = 'job_a_ap_pq_education_notgen'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApPqPersonalSkill(JobAApplicant):
    __tablename__ = 'job_a_ap_pq_personal_skill'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, server_default=text("'0'"))
    IS_SPECIAL_SKILL = Column(String(1))
    IS_DRIVING_SKILL = Column(String(1))
    SHORTHAND_WORD_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApplicantApplyVacancy(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_apply_vacancy'

    ID_APPLICANT_APPLY_VACANCY = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    NO_OF_APPLY = Column(Integer)
    CHOICE_RESPONSE_APPLY_STATUS = Column(String(1), server_default=text("'W'"))
    DATE_APPLICANT_APPLY = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobAApplicantBookmark(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_bookmark'

    ID_APPLICANT_BOOKMARK = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    BOOKMARK_DATE = Column(Date)
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobAApplicantBuySuperResume(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_buy_super_resume'

    ID_APPLICANT_BUY_SUPER_RESUME = Column(BigInteger, primary_key=True)
    ID_JOB_ORDERS = Column(ForeignKey(u'job_m_orders.ID_JOB_ORDERS'), index=True)
    ID_USER = Column(BigInteger)
    ID_SUPER_RESUME_FORMAT = Column(ForeignKey(u'job_n_super_resume_format.ID_SUPER_RESUME_FORMAT'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    COUNTRY_CODE = Column(String(3))
    QUANTITY = Column(Integer)
    USAGE = Column(Integer)
    ORDERS_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    EXPIRE_DATE = Column(Date)
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_m_order = relationship(u'JobMOrder')
    job_n_super_resume_format = relationship(u'JobNSuperResumeFormat')


class JobAApplicantCertificate(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_certificate'

    ID_APPLICANT_CERTIFICATE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_APPLICANT_CERTIFICATE_TYPE = Column(ForeignKey(u'job_n_applicant_certificate_type.ID_APPLICANT_CERTIFICATE_TYPE'), index=True)
    CERTIFICATE_NO = Column(String(255))
    GREEN_CARD_CATEGORY = Column(String(255))
    ID_COUNTRY_ISSUED_AT = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE_ISSUED_AT = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY_ISSUED_AT = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ISSUED_AT = Column(String(255))
    AUTHORIZED_BY = Column(String(255))
    ID_COUNTRY_PERMIT_OF_WORK = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE_PERMIT_OF_WORK = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    DATE_ISSUED = Column(Date)
    DATE_EXPIRE = Column(Date)
    ID_PASSPORT_TYPE = Column(ForeignKey(u'job_n_passport_type.ID_PASSPORT_TYPE'), index=True)
    ID_VISA_TYPE = Column(ForeignKey(u'job_n_visa_type.ID_VISA_TYPE'), index=True)
    FILE_PATH = Column(String(255))
    FILE_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_applicant_certificate_type = relationship(u'JobNApplicantCertificateType')
    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry', primaryjoin='JobAApplicantCertificate.ID_COUNTRY_ISSUED_AT == JobNCountry.ID_COUNTRY')
    job_n_country1 = relationship(u'JobNCountry', primaryjoin='JobAApplicantCertificate.ID_COUNTRY_PERMIT_OF_WORK == JobNCountry.ID_COUNTRY')
    job_n_passport_type = relationship(u'JobNPassportType')
    job_n_province = relationship(u'JobNProvince', primaryjoin='JobAApplicantCertificate.ID_PROVINCE_ISSUED_AT == JobNProvince.ID_PROVINCE')
    job_n_province1 = relationship(u'JobNProvince', primaryjoin='JobAApplicantCertificate.ID_PROVINCE_PERMIT_OF_WORK == JobNProvince.ID_PROVINCE')
    job_n_visa_type = relationship(u'JobNVisaType')


class JobAApplicantCertificateLang(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_certificate_lang'

    ID_APPLICANT_CERTIFICATE_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_CERTIFICATE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    GREEN_CARD_CATEGORY = Column(String(255))
    AUTHORIZED_BY = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApplicantCompany(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_company'

    ID_APPLICANT_COMPANY = Column(BigInteger, primary_key=True)
    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), index=True)
    COMPANY_NAME = Column(String(255))
    ID_BUSINESS_TYPE = Column(ForeignKey(u'job_n_business_type.ID_BUSINESS_TYPE'), index=True)
    ID_INDUSTRY_CATEGORY = Column(ForeignKey(u'job_n_industry_category.ID_INDUSTRY_CATEGORY'), index=True)
    ID_INDUSTRY = Column(ForeignKey(u'job_n_industry.ID_INDUSTRY'), index=True)
    ID_CORPORATE_SIZE = Column(ForeignKey(u'job_n_corporate_size.ID_CORPORATE_SIZE'), index=True)
    ID_NO_OF_EMPLOYEE = Column(ForeignKey(u'job_n_no_of_employee.ID_NO_OF_EMPLOYEE'), index=True)
    ID_BUSINESS_TURNOVER = Column(ForeignKey(u'job_n_business_turnover.ID_BUSINESS_TURNOVER'), index=True)
    ID_CURRENCY_BUSINESS_TURNOVER = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    BUSINESS_TURNOVER_MIN_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_MAX_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_RATE = Column(Numeric(20, 2))
    ID_PROFIT_PER_YEAR = Column(ForeignKey(u'job_n_profit_per_year.ID_PROFIT_PER_YEAR'), index=True)
    ID_CURRENCY_PROFIT_PER_YEAR = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    PROFIT_PER_YEAR_MIN_USD = Column(Numeric(20, 2))
    PROFIT_PER_YEAR_MAX_USD = Column(Numeric(20, 2))
    PROFIT_PER_YEAR_RATE = Column(Numeric(20, 2))
    ID_REGISTER_CAPITAL = Column(ForeignKey(u'job_n_register_capital.ID_REGISTER_CAPITAL'), index=True)
    ID_CURRENCY_REGISTER_CAPITAL = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    REGISTER_CAPITAL_MIN_USD = Column(Numeric(20, 2))
    REGISTER_CAPITAL_MAX_USD = Column(Numeric(20, 2))
    REGISTER_CAPITAL_RATE = Column(Numeric(20, 2))
    ID_PAID_UP_CAPITAL = Column(ForeignKey(u'job_n_paid_up_capital.ID_PAID_UP_CAPITAL'), index=True)
    ID_CURRENCY_PAID_UP_CAPITAL = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    PAID_UP_CAPITAL_MIN_USD = Column(Numeric(20, 2))
    PAID_UP_CAPITAL_MAX_USD = Column(Numeric(20, 2))
    PAID_UP_CAPITAL_RATE = Column(Numeric(20, 2))
    LOCAL_STAKEHOLDER_PERCENT = Column(Numeric(5, 2))
    FOREIGN_STAKEHOLDER_PERCENT = Column(Numeric(5, 2))
    PAR_VALUE_PER_SHARED = Column(Numeric(20, 2))
    HOUSING_NO = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE = Column(String(255))
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    TEL_PREFIX_NO = Column(String(255))
    TEL_NO = Column(String(255))
    TEL_EXT_NO = Column(String(255))
    MOBILE_PREFIX = Column(String(255))
    MOBILE_NO = Column(String(255))
    FAX_PREFIX_NO = Column(String(255))
    FAX_NO = Column(String(255))
    FAX_EXT_NO = Column(String(255))
    ID_GPS_TYPE = Column(ForeignKey(u'job_n_gps_type.ID_GPS_TYPE'), index=True)
    LAT = Column(String(255))
    LNG = Column(String(255))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_business_turnover = relationship(u'JobNBusinessTurnover')
    job_n_business_type = relationship(u'JobNBusinessType')
    job_n_city = relationship(u'JobNCity')
    job_c_corporate = relationship(u'JobCCorporate')
    job_n_corporate_size = relationship(u'JobNCorporateSize')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_currency = relationship(u'JobNCurrency', primaryjoin='JobAApplicantCompany.ID_CURRENCY_BUSINESS_TURNOVER == JobNCurrency.ID_CURRENCY')
    job_n_currency1 = relationship(u'JobNCurrency', primaryjoin='JobAApplicantCompany.ID_CURRENCY_PAID_UP_CAPITAL == JobNCurrency.ID_CURRENCY')
    job_n_currency2 = relationship(u'JobNCurrency', primaryjoin='JobAApplicantCompany.ID_CURRENCY_PROFIT_PER_YEAR == JobNCurrency.ID_CURRENCY')
    job_n_currency3 = relationship(u'JobNCurrency', primaryjoin='JobAApplicantCompany.ID_CURRENCY_REGISTER_CAPITAL == JobNCurrency.ID_CURRENCY')
    job_n_gps_type = relationship(u'JobNGpsType')
    job_n_industry = relationship(u'JobNIndustry')
    job_n_industry_category = relationship(u'JobNIndustryCategory')
    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_n_no_of_employee = relationship(u'JobNNoOfEmployee')
    job_n_paid_up_capital = relationship(u'JobNPaidUpCapital')
    job_n_profit_per_year = relationship(u'JobNProfitPerYear')
    job_n_province = relationship(u'JobNProvince')
    job_n_register_capital = relationship(u'JobNRegisterCapital')


class JobAApplicantCompanyLang(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_company_lang'

    ID_APPLICANT_COMPANY_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_COMPANY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    COMPANY_NAME = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApplicantComplainCorporate(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_complain_corporate'

    ID_APPLICANT_COMPLAIN_CORPORATE = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    ID_CORPORATE = Column(BigInteger, index=True)
    ID_VACANCY = Column(BigInteger)
    ID_APPLICANT_COMPLAIN = Column(ForeignKey(u'job_n_applicant_complain.ID_APPLICANT_COMPLAIN'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_applicant_complain = relationship(u'JobNApplicantComplain')


class JobAApplicantComplainVacancy(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_complain_vacancy'

    ID_APPLICANT_COMPLAIN_CORPORATE = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    ID_VACANCY = Column(BigInteger)
    ID_APPLICANT_COMPLAIN = Column(ForeignKey(u'job_n_applicant_complain.ID_APPLICANT_COMPLAIN'), index=True)
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_applicant_complain = relationship(u'JobNApplicantComplain')


class JobAApplicantCorporateViewProfile(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_corporate_view_profile'

    ID_APPLICANT_CORPORATE_VIEW_PROFILE = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), index=True)
    PROFILE_LANG_CODE3 = Column(String(3))
    VIEW_DATE = Column(DateTime)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_corporate = relationship(u'JobCCorporate')


class JobAApplicantCorporateViewTestScore(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_corporate_view_test_score'

    ID_APPLICANT_CORPORATE_VIEW_TEST_SCORE = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), index=True)
    ID_TEST = Column(BigInteger, index=True)
    VIEW_DATE = Column(DateTime)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_corporate = relationship(u'JobCCorporate')


class JobAApplicantFamily(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_family'

    ID_APPLICANT_FAMILY = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_APPLICANT_FAMILY_TYPE = Column(ForeignKey(u'job_n_applicant_family_type.ID_APPLICANT_FAMILY_TYPE'), index=True)
    SEQ = Column(SmallInteger)
    IDENTIFICATION_NO = Column(String(255))
    ID_PREFIX_NAME = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    ID_GENDER = Column(ForeignKey(u'job_n_gender.ID_GENDER'), index=True)
    IS_ALIVE = Column(String(1))
    DATE_DEAD = Column(DateTime)
    ID_DISEASES = Column(ForeignKey(u'job_n_diseases.ID_DISEASES'), index=True)
    DATE_BIRTH = Column(Date)
    ID_COUNTRY_BIRTH = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE_BIRTH = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY_BIRTH = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    CHOICE_LIVING_CONDITION = Column(String(1))
    CHOICE_WORKING_STATUS = Column(String(1))
    STUDY_INSTRUCTION_NAME = Column(String(255))
    ID_EDUCATION_LEVEL = Column(ForeignKey(u'job_n_education_level.ID_EDUCATION_LEVEL'), index=True)
    ID_CAREER = Column(ForeignKey(u'job_n_career.ID_CAREER'), index=True)
    ID_APPLICANT_COMPANY = Column(ForeignKey(u'job_a_applicant_company.ID_APPLICANT_COMPANY'), index=True)
    WORK_POSITION = Column(String(255))
    ID_SALARY_BASE = Column(ForeignKey(u'job_n_salary_base.ID_SALARY_BASE'), index=True)
    SALARY = Column(Numeric(20, 2))
    SALARY_USD = Column(Numeric(20, 2))
    SALARY_USD_RATE = Column(Numeric(20, 6))
    ID_CURRENCY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    ID_SALARY_PER_AMOUNT = Column(ForeignKey(u'job_n_salary_per_amount.ID_SALARY_PER_AMOUNT'), index=True)
    SALARY_PER_AMOUNTS = Column(Numeric(20, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_a_applicant_company = relationship(u'JobAApplicantCompany')
    job_n_applicant_family_type = relationship(u'JobNApplicantFamilyType')
    job_n_career = relationship(u'JobNCareer')
    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_currency = relationship(u'JobNCurrency')
    job_n_disease = relationship(u'JobNDisease')
    job_n_education_level = relationship(u'JobNEducationLevel')
    job_n_gender = relationship(u'JobNGender')
    job_n_prefix_name = relationship(u'JobNPrefixName')
    job_n_province = relationship(u'JobNProvince')
    job_n_salary_base = relationship(u'JobNSalaryBase')
    job_n_salary_per_amount = relationship(u'JobNSalaryPerAmount')


class JobAApplicantFamilyAddres(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_family_address'

    ID_APPLICANT_FAMILY_ADDRESS = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_APPLICANT_FAMILY = Column(ForeignKey(u'job_a_applicant_family.ID_APPLICANT_FAMILY'), index=True)
    ID_APPLICANT_ADDRESS_TYPE = Column(ForeignKey(u'job_n_applicant_address_type.ID_APPLICANT_ADDRESS_TYPE'), index=True)
    ID_HOUSE_LIVING_CONDITION = Column(ForeignKey(u'job_n_house_living_condition.ID_HOUSE_LIVING_CONDITION'), index=True)
    ID_HOUSE_HOUSING_TYPE = Column(ForeignKey(u'job_n_house_housing_type.ID_HOUSE_HOUSING_TYPE'), index=True)
    ID_HOUSE_PROPERTY_BELONGING = Column(ForeignKey(u'job_n_house_property_belonging.ID_HOUSE_PROPERTY_BELONGING'), index=True)
    ID_HOUSE_OWNERSHIP = Column(ForeignKey(u'job_n_house_ownership.ID_HOUSE_OWNERSHIP'), index=True)
    HOUSING_NO = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE = Column(String(255))
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    TEL_PREFIX_NO = Column(String(255))
    TEL_NO = Column(String(255))
    TEL_EXT_NO = Column(String(255))
    MOBILE_PREFIX_NO = Column(String(255))
    MOBILE_NO = Column(String(255))
    FAX_PREFIX_NO = Column(String(255))
    FAX_NO = Column(String(255))
    FAX_EXT_NO = Column(String(255))
    ID_GPS_TYPE = Column(ForeignKey(u'job_n_gps_type.ID_GPS_TYPE'), index=True)
    LAT = Column(String(255))
    LNG = Column(String(255))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_applicant_address_type = relationship(u'JobNApplicantAddressType')
    job_a_applicant_family = relationship(u'JobAApplicantFamily')
    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_gps_type = relationship(u'JobNGpsType')
    job_n_house_housing_type = relationship(u'JobNHouseHousingType')
    job_n_house_living_condition = relationship(u'JobNHouseLivingCondition')
    job_n_house_ownership = relationship(u'JobNHouseOwnership')
    job_n_house_property_belonging = relationship(u'JobNHousePropertyBelonging')
    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_n_province = relationship(u'JobNProvince')


class JobAApplicantFamilyAddressLang(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_family_address_lang'

    ID_APPLICANT_FAMILY_ADDRESS_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_FAMILY_ADDRESS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApplicantFamilyLang(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_family_lang'

    ID_APPLICANT_FAMILY_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_FAMILY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    STUDY_INSTRUCTION_NAME = Column(String(255))
    WORK_POSITION = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAApplicantImage(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_image'

    ID_APPLICANT_IMAGE = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_APPLICANT_IMAGE_TYPE = Column(ForeignKey(u'job_n_applicant_image_type.ID_APPLICANT_IMAGE_TYPE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_applicant_image_type = relationship(u'JobNApplicantImageType')


class JobAApplicantInviteInterview(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_invite_interview'

    ID_APPLICANT_INVITE_INTERVIEW = Column(BigInteger, primary_key=True)
    ID_USER_APPLICANT = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_USER_CORPORATE = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    CHOICE_FROM_SEARCH = Column(String(1))
    CHOICE_INTERVIEW = Column(String(1))
    DATE_INTERVIEW = Column(Date)
    DATE_INVITE_INTERVIEW = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser', primaryjoin='JobAApplicantInviteInterview.ID_USER_APPLICANT == SysMUser.ID_USER')
    sys_m_user1 = relationship(u'SysMUser', primaryjoin='JobAApplicantInviteInterview.ID_USER_CORPORATE == SysMUser.ID_USER')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobAApplicantInviteTest(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_invite_test'

    ID_APPLICANT_INVITE_TEST = Column(BigInteger, primary_key=True)
    ID_USER_APPLICANT = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_USER_CORPORATE = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_TEST = Column(ForeignKey(u'job_n_test.ID_TEST'), index=True)
    CHOICE_FROM_SEARCH = Column(String(1))
    CHOICE_INVITE_TEST = Column(String(1))
    DATE_INVITE_TEST = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_test = relationship(u'JobNTest')
    sys_m_user = relationship(u'SysMUser', primaryjoin='JobAApplicantInviteTest.ID_USER_APPLICANT == SysMUser.ID_USER')
    sys_m_user1 = relationship(u'SysMUser', primaryjoin='JobAApplicantInviteTest.ID_USER_CORPORATE == SysMUser.ID_USER')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobAApplicantInviteVacancy(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_invite_vacancy'

    ID_APPLICANT_INVITE_VACANCY = Column(BigInteger, primary_key=True)
    ID_USER_APPLICANT = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_USER_CORPORATE = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    CHOICE_FROM_SEARCH = Column(String(1))
    CHOICE_INVITE_VACANCY = Column(String(1))
    DATE_INVITE_VACANCY = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser', primaryjoin='JobAApplicantInviteVacancy.ID_USER_APPLICANT == SysMUser.ID_USER')
    sys_m_user1 = relationship(u'SysMUser', primaryjoin='JobAApplicantInviteVacancy.ID_USER_CORPORATE == SysMUser.ID_USER')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobAApplicantProfileLanguage(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_profile_language'

    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), primary_key=True, nullable=False)
    LANG_CODE3 = Column(String(3), primary_key=True, nullable=False)
    IS_DEFAULT_LANGUAGE = Column(String(1))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')


class JobAApplicantRecommendVacancy(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_recommend_vacancy'

    ID_APPLICANT_RECOMMEND_VACANCY = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    EMAIL_SENDER_RECOMMEND = Column(String(255))
    NAME_RECEIVER_RECOMMEND = Column(String(255))
    EMAIL_RECEIVER_RECOMMEND = Column(String(255))
    DESCRIPTION = Column(Text)
    SEND_DATE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobAApplicantRecommendVacancyLang(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_recommend_vacancy_lang'

    ID_APPLICANT_RECOMMEND_VACANCY_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_RECOMMEND_VACANCY = Column(ForeignKey(u'job_a_applicant_recommend_vacancy.ID_APPLICANT_RECOMMEND_VACANCY'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    EMAIL_SENDER_RECOMMEND = Column(String(255))
    EMAIL_RECEIVER_RECOMMEND = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant_recommend_vacancy = relationship(u'JobAApplicantRecommendVacancy')


class JobAApplicantTestScore(DeclarativeBase2):
    __tablename__ = 'job_a_applicant_test_score'

    ID_APPLICANT_TEST_SCORE = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger)
    ID_TEST = Column(ForeignKey(u'job_n_test.ID_TEST'), index=True)
    SCORE = Column(Numeric(20, 2))
    CHOICE_BUY_TEST = Column(String(1))
    TEST_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    EXPIRE_DATE = Column(Date)
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_n_test = relationship(u'JobNTest')


class JobAHealthProfile(DeclarativeBase2):
    __tablename__ = 'job_a_health_profile'

    ID_HEALTH_PROFILE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    ID_APPLICANT = Column(BigInteger)
    YEAR = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAHpAnswer(DeclarativeBase2):
    __tablename__ = 'job_a_hp_answer'

    ID_HP_ANSWER = Column(BigInteger, primary_key=True)
    ID_HEALTH_QUESTION_ANSWER = Column(ForeignKey(u'job_n_health_question_answer.ID_HEALTH_QUESTION_ANSWER'), index=True)
    ANSWER = Column(String(255))
    ID_HEALTH_ANSWER_TYPE = Column(ForeignKey(u'job_n_health_answer_type.ID_HEALTH_ANSWER_TYPE'), index=True)
    ID_HEALTH_PROFILE = Column(ForeignKey(u'job_a_health_profile.ID_HEALTH_PROFILE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_health_answer_type = relationship(u'JobNHealthAnswerType')
    job_a_health_profile = relationship(u'JobAHealthProfile')
    job_n_health_question_answer = relationship(u'JobNHealthQuestionAnswer')


class JobAManageCriterion(DeclarativeBase2):
    __tablename__ = 'job_a_manage_criteria'

    ID_MANAGE_CRITERIA = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_CAREER = Column(ForeignKey(u'job_n_career.ID_CAREER'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    ID_JOB_POSITION = Column(ForeignKey(u'job_n_job_position.ID_JOB_POSITION'), index=True)
    CHOICE_SALARY = Column(String(1))
    ID_CURRENCY_BUSINESS = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    ID_CURRENCY_SALARY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    IS_WILLWORK_ABORD = Column(String(1))
    IS_WILLWORK_DOMESTIC = Column(String(1))
    IS_HAVE_VEHICLE = Column(String(1))
    IS_TRAVELLING = Column(String(1))
    CHOICE_TRAVELLING = Column(String(1))
    CHOICE_TRAVELLING_ON_SITE = Column(String(1))
    CHOICE_START_WORKING = Column(String(1))
    ID_READY_WORK = Column(ForeignKey(u'job_n_ready_work.ID_READY_WORK'), index=True)
    DATE_START_WORKING = Column(Date)
    ID_REPEAT_TIME = Column(ForeignKey(u'job_n_repeat_time.ID_REPEAT_TIME'), index=True)
    ID_PERCENT_MATCH = Column(ForeignKey(u'job_n_percent_match.ID_PERCENT_MATCH'), index=True)
    IS_WORK_IN_REGISTERED_ADDRESS = Column(String(1))
    CHOICE_INTENTION = Column(String(1))
    SENT_TIME = Column(Time)
    SQL_MATCH = Column(Text)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_n_career = relationship(u'JobNCareer')
    job_n_currency = relationship(u'JobNCurrency', primaryjoin='JobAManageCriterion.ID_CURRENCY_BUSINESS == JobNCurrency.ID_CURRENCY')
    job_n_currency1 = relationship(u'JobNCurrency', primaryjoin='JobAManageCriterion.ID_CURRENCY_SALARY == JobNCurrency.ID_CURRENCY')
    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    job_n_job_position = relationship(u'JobNJobPosition')
    job_n_percent_match = relationship(u'JobNPercentMatch')
    job_n_ready_work = relationship(u'JobNReadyWork')
    job_n_repeat_time = relationship(u'JobNRepeatTime')


class JobAMcWillingWork(JobAManageCriterion):
    __tablename__ = 'job_a_mc_willing_work'

    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), primary_key=True, server_default=text("'0'"))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAMcCorporateTypeSize(JobAManageCriterion):
    __tablename__ = 'job_a_mc_corporate_type_size'

    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), primary_key=True, server_default=text("'0'"))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobAMcCtBusinessTurnover(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ct_business_turnover'

    ID_MC_CT_BUSINESS_TURNOVER = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_BUSINESS_TURNOVER = Column(ForeignKey(u'job_n_business_turnover.ID_BUSINESS_TURNOVER'), index=True)
    BUSINESS_TURNOVER_MIN_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_MAN_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_RATE = Column(Numeric(20, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_business_turnover = relationship(u'JobNBusinessTurnover')
    job_a_manage_criterion = relationship(u'JobAManageCriterion')


class JobAMcCtBusinessType(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ct_business_type'

    ID_MC_CT_BUSINESS_TYPE = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_BUSINESS_TYPE = Column(ForeignKey(u'job_n_business_type.ID_BUSINESS_TYPE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_business_type = relationship(u'JobNBusinessType')
    job_a_manage_criterion = relationship(u'JobAManageCriterion')


class JobAMcCtIndustryCategory(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ct_industry_category'

    ID_MC_CT_INDUSTRY_CATEGORY = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_INDUSTRY_CATEGORY = Column(ForeignKey(u'job_n_industry_category.ID_INDUSTRY_CATEGORY'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_industry_category = relationship(u'JobNIndustryCategory')
    job_a_manage_criterion = relationship(u'JobAManageCriterion')


class JobAMcCtNoOfEmployee(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ct_no_of_employee'

    ID_MC_CT_NO_OF_EMPLOYEE = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_NO_OF_EMPLOYEE = Column(ForeignKey(u'job_n_no_of_employee.ID_NO_OF_EMPLOYEE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_manage_criterion = relationship(u'JobAManageCriterion')
    job_n_no_of_employee = relationship(u'JobNNoOfEmployee')


class JobAMcCtRegisterCapital(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ct_register_capital'

    ID_MC_CT_REGISTER_CAPITAL = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_REGISTER_CAPITAL = Column(ForeignKey(u'job_n_register_capital.ID_REGISTER_CAPITAL'), index=True)
    REGISTER_CAPITAL_MIN_USD = Column(Numeric(20, 2))
    REGISTER_CAPITAL_MAX_USD = Column(Numeric(20, 2))
    REGISTER_CAPITAL_RATE = Column(Numeric(20, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_manage_criterion = relationship(u'JobAManageCriterion')
    job_n_register_capital = relationship(u'JobNRegisterCapital')


class JobAMcEmploymentTask(DeclarativeBase2):
    __tablename__ = 'job_a_mc_employment_task'

    ID_MC_EMPLOYMENT_TASK = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_EMPLOYMENT_TYPE = Column(ForeignKey(u'job_n_employment_type.ID_EMPLOYMENT_TYPE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_employment_type = relationship(u'JobNEmploymentType')
    job_a_manage_criterion = relationship(u'JobAManageCriterion')


class JobAMcEtTaskTime(DeclarativeBase2):
    __tablename__ = 'job_a_mc_et_task_time'

    ID_MC_ET_TASK_TIME = Column(BigInteger, primary_key=True)
    ID_MC_EMPLOYMENT_TASK = Column(ForeignKey(u'job_a_mc_employment_task.ID_MC_EMPLOYMENT_TASK'), index=True)
    ID_DAY = Column(ForeignKey(u'job_n_day.ID_DAY'), index=True)
    TIME_START = Column(Time)
    TIME_END = Column(Time)
    TIME_DURATION_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_day = relationship(u'JobNDay')
    job_a_mc_employment_task = relationship(u'JobAMcEmploymentTask')


class JobAMcFringeBenefit(DeclarativeBase2):
    __tablename__ = 'job_a_mc_fringe_benefit'

    ID_MC_FRINGE_BENEFIT = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_FRINGE_BENEFIT_TYPE = Column(ForeignKey(u'job_n_fringe_benefit_type.ID_FRINGE_BENEFIT_TYPE'), index=True)
    ID_FRINGE_BENEFIT = Column(ForeignKey(u'job_n_fringe_benefit.ID_FRINGE_BENEFIT'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_fringe_benefit = relationship(u'JobNFringeBenefit')
    job_n_fringe_benefit_type = relationship(u'JobNFringeBenefitType')
    job_a_manage_criterion = relationship(u'JobAManageCriterion')


class JobAMcSalaryBase(DeclarativeBase2):
    __tablename__ = 'job_a_mc_salary_base'

    ID_MC_SALARY_BASE = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_SALARY_BASE = Column(ForeignKey(u'job_n_salary_base.ID_SALARY_BASE'), index=True)
    IS_NEGOTIABLE = Column(String(1))
    SALARY_FROM = Column(Numeric(20, 2))
    SALARY_FROM_USD = Column(Numeric(20, 2))
    SALARY_FROM_USD_RATE = Column(Numeric(20, 6))
    SALARY_TO = Column(Numeric(20, 2))
    SALARY_TO_USD = Column(Numeric(20, 2))
    SALARY_TO_USD_RATE = Column(Numeric(20, 6))
    ID_SALARY_PER_AMOUNT = Column(ForeignKey(u'job_n_salary_per_amount.ID_SALARY_PER_AMOUNT'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_manage_criterion = relationship(u'JobAManageCriterion')
    job_n_salary_base = relationship(u'JobNSalaryBase')
    job_n_salary_per_amount = relationship(u'JobNSalaryPerAmount')


class JobAMcVehicle(DeclarativeBase2):
    __tablename__ = 'job_a_mc_vehicle'

    ID_MC_VEHICLE = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    ID_VEHICLE = Column(ForeignKey(u'job_n_vehicle.ID_VEHICLE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_manage_criterion = relationship(u'JobAManageCriterion')
    job_n_vehicle = relationship(u'JobNVehicle')


class JobAMcWwWorkPlace(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ww_work_place'

    ID_MC_WW_WORK_PLACE = Column(BigInteger, primary_key=True)
    ID_MANAGE_CRITERIA = Column(ForeignKey(u'job_a_manage_criteria.ID_MANAGE_CRITERIA'), index=True)
    CHOICE_WORK = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_manage_criterion = relationship(u'JobAManageCriterion')


class JobAMcWwWpCountry(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ww_wp_country'

    ID_MC_WW_WP_COUNTRY = Column(BigInteger, primary_key=True)
    ID_MC_WW_WORK_PLACE = Column(ForeignKey(u'job_a_mc_ww_work_place.ID_MC_WW_WORK_PLACE'), index=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    IS_WORK_PERMIT = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_a_mc_ww_work_place = relationship(u'JobAMcWwWorkPlace')
    job_n_province = relationship(u'JobNProvince')


class JobAMcWwWpIndustryEstate(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ww_wp_industry_estate'

    ID_MC_WW_WP_INDUSTRY_ESTATE = Column(BigInteger, primary_key=True)
    ID_MC_WW_WORK_PLACE = Column(ForeignKey(u'job_a_mc_ww_work_place.ID_MC_WW_WORK_PLACE'), index=True)
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_a_mc_ww_work_place = relationship(u'JobAMcWwWorkPlace')


class JobAMcWwWpPublicTransportation(DeclarativeBase2):
    __tablename__ = 'job_a_mc_ww_wp_public_transportation'

    ID_MC_WW_WP_PUBLIC_TRANSPORTATION = Column(BigInteger, primary_key=True)
    ID_MC_WW_WORK_PLACE = Column(ForeignKey(u'job_a_mc_ww_work_place.ID_MC_WW_WORK_PLACE'), index=True)
    ID_PUBLIC_TRANSPORTATION = Column(ForeignKey(u'job_n_public_transportation.ID_PUBLIC_TRANSPORTATION'), index=True)
    ID_UNIT_LENGTH = Column(ForeignKey(u'job_n_unit_length.ID_UNIT_LENGTH'), index=True)
    UNIT = Column(Integer)
    UNIT_METER = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_mc_ww_work_place = relationship(u'JobAMcWwWorkPlace')
    job_n_public_transportation = relationship(u'JobNPublicTransportation')
    job_n_unit_length = relationship(u'JobNUnitLength')


class JobCApplicantPurchaseOrder(DeclarativeBase2):
    __tablename__ = 'job_c_applicant_purchase_order'

    ID_APPLICANT_PURCHASE_ORDER = Column(BigInteger, primary_key=True)
    ID_APPLICANT = Column(BigInteger)
    ID_PACKAGE = Column(BigInteger)
    ID_BUDGET = Column(BigInteger)
    ID_ORDER = Column(BigInteger)
    ID_PROMOTION = Column(BigInteger)
    PRICE_TOTAL = Column(Numeric(20, 6))
    QUANTITY = Column(Integer)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCApplicantPurchaseOrderProduct(DeclarativeBase2):
    __tablename__ = 'job_c_applicant_purchase_order_product'

    ID_APPLICANT_PURCHASE_ORDER_PRODUCT = Column(BigInteger, primary_key=True)
    ID_APPLICANT_PURCHASE_ORDER = Column(ForeignKey(u'job_c_applicant_purchase_order.ID_APPLICANT_PURCHASE_ORDER'), index=True)
    ID_PRODUCT_TYPE = Column(BigInteger)
    ID_PRODUCT = Column(BigInteger)
    PRICE = Column(Numeric(20, 6))
    QUANTITY = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_applicant_purchase_order = relationship(u'JobCApplicantPurchaseOrder')


class JobCBaPersonalInfo(DeclarativeBase2):
    __tablename__ = 'job_c_ba_personal_info'

    ID_BA_PERSONAL_INFO = Column(BigInteger, primary_key=True)
    ID_BUY_APPLICANT = Column(ForeignKey(u'job_c_buy_applicant.ID_BUY_APPLICANT'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_buy_applicant = relationship(u'JobCBuyApplicant')


class JobCBuyApplicant(DeclarativeBase2):
    __tablename__ = 'job_c_buy_applicant'

    ID_BUY_APPLICANT = Column(BigInteger, primary_key=True)
    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), index=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    job_c_corporate = relationship(u'JobCCorporate')


class JobCCoCertificateLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_certificate_lang'

    ID_CO_CERTIFICATE_LANG = Column(BigInteger, primary_key=True)
    ID_CO_CERTIFICATE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    CERTIFICATE_NUMBER = Column(String(255))
    FILE_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCoIdAddressLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_address_lang'

    ID_CO_ID_ADDRESS_LANG = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCoIdCertificate(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_certificate'

    ID_CO_ID_CERTIFICATE = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(ForeignKey(u'job_c_co_identity.ID_CO_IDENTITY'), index=True)
    ID_CORPORATE_CERTIFICATE_TYPE = Column(ForeignKey(u'job_n_corporate_certificate_type.ID_CORPORATE_CERTIFICATE_TYPE'), index=True)
    CERTIFICATE_NUMBER = Column(String(255))
    ISSUED_BY = Column(String(255))
    ISSUED_AT = Column(String(255))
    DATE_ISSUED = Column(Date)
    DATE_EXPIRE = Column(Date)
    FILE_PATH = Column(String(255))
    FILE_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_corporate_certificate_type = relationship(u'JobNCorporateCertificateType')
    job_c_co_identity = relationship(u'JobCCoIdentity')


class JobCCoIdCertificateLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_certificate_lang'

    ID_CO_ID_CERTIFICATE_LANG = Column(BigInteger, primary_key=True)
    ID_CO_ID_CERTIFICATE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    CERTIFICATE_NUMBER = Column(String(255))
    FILE_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCoIdContactPerson(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_contact_person'

    ID_CO_ID_CONTACT_PERSON = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(ForeignKey(u'job_c_co_identity.ID_CO_IDENTITY'), index=True)
    CHOICE_CONTACT_PERSON_TYPE = Column(String(1))
    ID_PREFIX_NAME = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    ID_CAREER = Column(ForeignKey(u'job_n_career.ID_CAREER'), index=True)
    POSITION_NAME = Column(String(255))
    EMAIL = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255, u'utf8_unicode_ci'))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255, u'utf8_unicode_ci'))

    job_n_career = relationship(u'JobNCareer')
    job_c_co_identity = relationship(u'JobCCoIdentity')
    job_n_prefix_name = relationship(u'JobNPrefixName')


class JobCCoIdContactPersonLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_contact_person_lang'

    ID_CO_ID_CONTACT_PERSON_LANG = Column(BigInteger, primary_key=True)
    ID_CO_ID_CONTACT_PERSON = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    NICK_NAME = Column(String(255))
    POSITION_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCoIdCpContactPhone(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_cp_contact_phone'

    ID_CO_ID_CP_CONTACT_PHONE = Column(BigInteger, primary_key=True)
    ID_CO_ID_CONTACT_PERSON = Column(ForeignKey(u'job_c_co_id_contact_person.ID_CO_ID_CONTACT_PERSON'), index=True)
    ID_PHONE_TYPE = Column(ForeignKey(u'job_n_phone_type.ID_PHONE_TYPE'), index=True)
    PHONE_PREFIX = Column(String(255))
    PHONE_NUMBER = Column(String(255))
    PHONE_EXT = Column(String(255))
    TIME_START = Column(Time)
    TIME_END = Column(Time)
    TIME_DURATION_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_co_id_contact_person = relationship(u'JobCCoIdContactPerson')
    job_n_phone_type = relationship(u'JobNPhoneType')


class JobCCoIdCpSocialNetwork(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_cp_social_network'

    ID_CO_ID_CP_SOCIAL_NETWORK = Column(BigInteger, primary_key=True)
    ID_CO_ID_CONTACT_PERSON = Column(ForeignKey(u'job_c_co_id_contact_person.ID_CO_ID_CONTACT_PERSON'), index=True)
    ID_SOCIAL_NETWORK = Column(ForeignKey(u'job_n_social_network.ID_SOCIAL_NETWORK'), index=True)
    SOCIAL_PROFILE_ID = Column(String(255))
    SOCIAL_OAUTH_TOKEN = Column(String(255))
    SOCIAL_OAUTH_SECRET_TOKEN = Column(String(255))
    SOCIAL_ACCOUNT_NAME = Column(String(255))
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_co_id_contact_person = relationship(u'JobCCoIdContactPerson')
    job_n_social_network = relationship(u'JobNSocialNetwork')


class JobCCoIdCpSocialNetworkLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_cp_social_network_lang'

    ID_CO_ID_CP_SOCIAL_NETWORK_LANG = Column(BigInteger, primary_key=True)
    ID_CO_ID_CP_SOCIAL_NETWORK = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCoIdFringeBenefit(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_fringe_benefit'

    ID_CO_ID_FRINGE_BENEFIT = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(ForeignKey(u'job_c_co_identity.ID_CO_IDENTITY'), index=True)
    ID_FRINGE_BENEFIT_TYPE = Column(ForeignKey(u'job_n_fringe_benefit_type.ID_FRINGE_BENEFIT_TYPE'), index=True)
    ID_FRINGE_BENEFIT = Column(ForeignKey(u'job_n_fringe_benefit.ID_FRINGE_BENEFIT'), index=True)
    STATUS = Column(String(1, u'utf8_unicode_ci'), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255, u'utf8_unicode_ci'))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255, u'utf8_unicode_ci'))

    job_c_co_identity = relationship(u'JobCCoIdentity')
    job_n_fringe_benefit = relationship(u'JobNFringeBenefit')
    job_n_fringe_benefit_type = relationship(u'JobNFringeBenefitType')


class JobCCoIdSocialNetwork(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_social_network'

    ID_CO_ID_SOCIAL_NETWORK = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(ForeignKey(u'job_c_co_identity.ID_CO_IDENTITY'), index=True)
    ID_SOCIAL_NETWORK = Column(ForeignKey(u'job_n_social_network.ID_SOCIAL_NETWORK'), index=True)
    SOCIAL_PROFILE_ID = Column(String(255))
    SOCIAL_OAUTH_TOKEN = Column(String(255))
    SOCIAL_OAUTH_SECRET_TOKEN = Column(String(255))
    SOCIAL_ACCOUNT_NAME = Column(String(255))
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_co_identity = relationship(u'JobCCoIdentity')
    job_n_social_network = relationship(u'JobNSocialNetwork')


class JobCCoIdSocialNetworkLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_social_network_lang'

    ID_CO_ID_SOCIAL_NETWORK_LANG = Column(BigInteger, primary_key=True)
    ID_CO_ID_SOCIAL_NETWORK = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCoIdWorkingDay(DeclarativeBase2):
    __tablename__ = 'job_c_co_id_working_day'

    ID_CO_ID_WORKING_DAY = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(ForeignKey(u'job_c_co_identity.ID_CO_IDENTITY'), index=True)
    ID_DAY = Column(ForeignKey(u'job_n_day.ID_DAY'), index=True)
    TIME_START = Column(Time)
    TIME_END = Column(Time)
    TIME_DURATION_MINUTE = Column(Integer)
    STATUS = Column(String(1, u'utf8_unicode_ci'), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255, u'utf8_unicode_ci'))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255, u'utf8_unicode_ci'))

    job_c_co_identity = relationship(u'JobCCoIdentity')
    job_n_day = relationship(u'JobNDay')


class JobCCoIdentity(DeclarativeBase2):
    __tablename__ = 'job_c_co_identity'

    ID_CO_IDENTITY = Column(BigInteger, primary_key=True)
    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), index=True)
    CHOICE_CORPORATE_TYPE = Column(String(1))
    CORPORATE_OF_COUNTRY_NO = Column(String(255))
    IS_SAME_COMPANY_IDENTITY = Column(String(1))
    IS_SAME_COMPANY_IDENTITY_CONTACT_MODES = Column(String(1))
    IS_SAME_COMPANY_IDENTITY_CONTACT_PERSON = Column(String(1))
    IS_SAME_COMPANY_REGISTER = Column(String(1))
    IS_SAME_COMPANY_TAX_EXCISE = Column(String(1))
    IS_SAME_COMPANY_TAX_REVENUE = Column(String(1))
    IS_SAME_COMPANY_TAX_VAT = Column(String(1))
    IS_SAME_COMPANY_VISION_MISSION = Column(String(1))
    IS_SAME_COMPANY_TYPE_SIZE_BUSINESS_TYPE = Column(String(1))
    IS_SAME_COMPANY_TYPE_SIZE_BUSINESS = Column(String(1))
    IS_SAME_COMPANY_TYPE_SIZE_PER_VALUE = Column(String(1))
    IS_SAME_COMPANY_TYPE_SIZE_END_PRODUCT = Column(String(1))
    IS_SAME_COMPANY_WORKING = Column(String(1))
    IS_SAME_COMPANY_FRINGE_BENEFIT = Column(String(1))
    IMAGE_LOGO_PATH = Column(String(255))
    IMAGE_LOGO_NAME = Column(String(255))
    ID_COUNTRY_ESTABLISHED = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE_ESTABLISHED = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY_ESTABLISHED = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY_ESTABLISHED = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    CHOICE_COMPANY_TYPE = Column(String(1))
    COMPANY_NAME = Column(String(255))
    COMPANY_NAME_ENG = Column(String(255))
    CORPORATE_WEBSITE = Column(String(255))
    DATE_ESTABLISHED = Column(Date)
    ID_LANGUAGE_SPOKEN = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    CORPORATE_VISION = Column(Text)
    CORPORATE_MISSION = Column(Text)
    CORPORATE_ACHIEVEMENT = Column(Text)
    CORPORATE_DESCRIPTION = Column(Text)
    IMAGE_VISION_PATH = Column(String(255))
    IMAGE_VISION_NAME = Column(String(255))
    ID_BUSINESS_TYPE = Column(ForeignKey(u'job_n_business_type.ID_BUSINESS_TYPE'), index=True)
    ID_INDUSTRY_CATEGORY = Column(ForeignKey(u'job_n_industry_category.ID_INDUSTRY_CATEGORY'), index=True)
    ID_INDUSTRY = Column(ForeignKey(u'job_n_industry.ID_INDUSTRY'), index=True)
    ID_CORPORATE_SIZE = Column(ForeignKey(u'job_n_corporate_size.ID_CORPORATE_SIZE'), index=True)
    ID_NO_OF_EMPLOYEE = Column(ForeignKey(u'job_n_no_of_employee.ID_NO_OF_EMPLOYEE'), index=True)
    ID_BUSINESS_TURNOVER = Column(ForeignKey(u'job_n_business_turnover.ID_BUSINESS_TURNOVER'), index=True)
    ID_CURRENCY_BUSINESS_TURNOVER = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    BUSINESS_TURNOVER_MIN_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_MAX_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_RATE = Column(Numeric(20, 2))
    ID_PROFIT_PER_YEAR = Column(ForeignKey(u'job_n_profit_per_year.ID_PROFIT_PER_YEAR'), index=True)
    ID_CURRENCY_PROFIT_PER_YEAR = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    PROFIT_PER_YEAR_MIN_USD = Column(Numeric(20, 2))
    PROFIT_PER_YEAR_MAX_USD = Column(Numeric(20, 2))
    PROFIT_PER_YEAR_RATE = Column(Numeric(20, 2))
    ID_REGISTER_CAPITAL = Column(ForeignKey(u'job_n_register_capital.ID_REGISTER_CAPITAL'), index=True)
    ID_CURRENCY_REGISTER_CAPITAL = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    REGISTER_CAPITAL_MIN_USD = Column(Numeric(20, 2))
    REGISTER_CAPITAL_MAX_USD = Column(Numeric(20, 2))
    REGISTER_CAPITAL_RATE = Column(Numeric(20, 2))
    ID_PAID_UP_CAPITAL = Column(ForeignKey(u'job_n_paid_up_capital.ID_PAID_UP_CAPITAL'), index=True)
    ID_CURRENCY_PAID_UP_CAPITAL = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    PAID_UP_REGISTER_CAPITAL_MIN_USD = Column(Numeric(20, 2))
    PAID_UP_REGISTER_CAPITAL_MAX_USD = Column(Numeric(20, 2))
    PAID_UP_REGISTER_CAPITAL_RATE = Column(Numeric(20, 2))
    LOCAL_STAKEHOLDER_PERCENT = Column(Numeric(5, 2))
    FOREIGN_STAKEHOLDER_PERCENT = Column(Numeric(5, 2))
    PER_VALUE_PER_SHARE = Column(Numeric(20, 2))
    CHOICE_END_PRODUCT = Column(String(1))
    IS_INDUSTRIAL_PRODUCT = Column(String(1))
    ID_INDUSTRIAL_PRODUCT = Column(ForeignKey(u'job_n_industrial_product.ID_INDUSTRIAL_PRODUCT'), index=True)
    IS_CONSUMER_PRODUCT = Column(String(1))
    ID_CONSUMER_PRODUCT = Column(ForeignKey(u'job_n_consumer_product.ID_CONSUMER_PRODUCT'), index=True)
    NO_WORKING_DAY_PER_WEEK = Column(Integer)
    NO_WORKING_HOUR_PER_DAY = Column(Integer)
    CHOICE_NAME_INVOICE = Column(String(1))
    NAME_INVOICE = Column(String(255))
    NAME_INVOICE_ENG = Column(String(255))
    CHOICE_ADDRESS = Column(String(1))
    IS_TAX_REVENUE = Column(String(1))
    TAX_REVENUE_NO = Column(String(255))
    IS_TAX_EXCISE = Column(String(1))
    TAX_EXCISE_NO = Column(String(255))
    IS_TAX_VAT = Column(String(1))
    TAX_VAT_NO = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_business_turnover = relationship(u'JobNBusinessTurnover')
    job_n_business_type = relationship(u'JobNBusinessType')
    job_n_city = relationship(u'JobNCity')
    job_n_consumer_product = relationship(u'JobNConsumerProduct')
    job_c_corporate = relationship(u'JobCCorporate')
    job_n_corporate_size = relationship(u'JobNCorporateSize')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_currency = relationship(u'JobNCurrency', primaryjoin='JobCCoIdentity.ID_CURRENCY_BUSINESS_TURNOVER == JobNCurrency.ID_CURRENCY')
    job_n_currency1 = relationship(u'JobNCurrency', primaryjoin='JobCCoIdentity.ID_CURRENCY_PAID_UP_CAPITAL == JobNCurrency.ID_CURRENCY')
    job_n_currency2 = relationship(u'JobNCurrency', primaryjoin='JobCCoIdentity.ID_CURRENCY_PROFIT_PER_YEAR == JobNCurrency.ID_CURRENCY')
    job_n_currency3 = relationship(u'JobNCurrency', primaryjoin='JobCCoIdentity.ID_CURRENCY_REGISTER_CAPITAL == JobNCurrency.ID_CURRENCY')
    job_n_industrial_product = relationship(u'JobNIndustrialProduct')
    job_n_industry = relationship(u'JobNIndustry')
    job_n_industry_category = relationship(u'JobNIndustryCategory')
    job_n_language = relationship(u'JobNLanguage')
    job_n_no_of_employee = relationship(u'JobNNoOfEmployee')
    job_n_paid_up_capital = relationship(u'JobNPaidUpCapital')
    job_n_profit_per_year = relationship(u'JobNProfitPerYear')
    job_n_province = relationship(u'JobNProvince')
    job_n_register_capital = relationship(u'JobNRegisterCapital')


class JobCCoIdAddres(JobCCoIdentity):
    __tablename__ = 'job_c_co_id_address'

    ID_CO_IDENTITY = Column(ForeignKey(u'job_c_co_identity.ID_CO_IDENTITY'), primary_key=True, index=True)
    HOUSING_NO = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE = Column(String(255))
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    TEL_PREFIX_NO = Column(String(255))
    TEL_NO = Column(String(255))
    TEL_EXT_NO = Column(String(255))
    MOBILE_PREFIX_NO = Column(String(255))
    MOBILE_NO = Column(String(255))
    FAX_PERFIX_NO = Column(String(255))
    FAX_NO = Column(String(255))
    FAX_EXT_NO = Column(String(255))
    ID_GPS_TYPE = Column(ForeignKey(u'job_n_gps_type.ID_GPS_TYPE'), index=True)
    LAT = Column(String(255))
    LNG = Column(String(255))
    DESCRIPTION = Column(Text)
    EMAIL = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_gps_type = relationship(u'JobNGpsType')
    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_n_province = relationship(u'JobNProvince')


class JobCCoIdentityLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_identity_lang'

    ID_CO_IDENTITY_LANG = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    IMAGE_LOGO_NAME = Column(String(255))
    COMPANY_NAME = Column(String(255))
    IMAGE_VISION_NAME = Column(String(255))
    NAME_INVOICE = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCoInvoiceLang(DeclarativeBase2):
    __tablename__ = 'job_c_co_invoice_lang'

    ID_CO_INVOICE_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME_INVOICE = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    SRTEET_ADDRESS2 = Column(String(255))
    TAX_REVENUE = Column(String(255))
    TAX_EXCISE = Column(String(255))
    TAX_VAT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCorpoarteBusRoute(DeclarativeBase2):
    __tablename__ = 'job_c_corpoarte_bus_route'

    ID_CORPOARTE_BUS_ROUTE = Column(BigInteger, primary_key=True)
    ID_CO_IDENTITY = Column(ForeignKey(u'job_c_co_identity.ID_CO_IDENTITY'), index=True)
    ID_BUS_ROUTE = Column(BigInteger)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_co_identity = relationship(u'JobCCoIdentity')


class JobCCorporate(DeclarativeBase2):
    __tablename__ = 'job_c_corporate'

    ID_CORPORATE = Column(BigInteger, primary_key=True)
    CHOICE_INVOICE = Column(String(1, u'utf8_unicode_ci'))
    NAME_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    NAME_INVOICE_ENG = Column(String(255, u'utf8_unicode_ci'))
    HOUSING_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    STREET_ADDRESS1_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    STREET_ADDRESS2_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    ID_COUNTRY_INVOICE = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE_INVOICE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY_INVOICE = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY_INVOICE = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    IS_TAX_REVENUE_INVOICE = Column(String(1, u'utf8_unicode_ci'))
    TAX_REVENUE_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    IS_TAX_EXCISE_INVOICE = Column(String(1, u'utf8_unicode_ci'))
    TAX_EXCISE_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    IS_TAX_VAT_INVOICE = Column(String(1, u'utf8_unicode_ci'))
    TAX_VAT_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    TEL_PREFIX_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    TEL_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    TEL_EXT_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    MOBILE_PREFIX_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    MOBILE_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    FAX_PERFIX_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    FAX_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    FAX_EXT_NO_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    EMAIL_INVOICE = Column(String(255, u'utf8_unicode_ci'))
    STATUS = Column(String(1, u'utf8_unicode_ci'), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255, u'utf8_unicode_ci'))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255, u'utf8_unicode_ci'))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_province = relationship(u'JobNProvince')


class JobCCorporateAddressLang(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_address_lang'

    ID_CORPORATE_ADDRESS_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE_ADDRESS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCorporateBookmark(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_bookmark'

    ID_CORPORATE_BOOKMARK = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    CHOICE_FROM_SEARCH = Column(String(1))
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    BOOKMARK_DATE = Column(Date)
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    sys_m_user = relationship(u'SysMUser')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCCorporateBuyProfile(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_buy_profile'

    ID_CORPORATE_BUY_PROFILE = Column(BigInteger, primary_key=True)
    ID_JOB_ORDERS = Column(ForeignKey(u'job_m_orders.ID_JOB_ORDERS'), index=True)
    ID_USER_COPRORATE = Column(BigInteger)
    ID_USER_APPLICANT = Column(BigInteger)
    PROFILE_LANG_CODE3 = Column(String(3))
    ORDERS_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    EXPIRE_DATE = Column(Date)
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_m_order = relationship(u'JobMOrder')


class JobCCorporateComplainApplicant(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_complain_applicant'

    ID_CORPORATE_COMPLAIN_APPLICANT = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    ID_USER_APPLICANT = Column(BigInteger, index=True)
    ID_CORPORATE_COMPLAIN = Column(ForeignKey(u'job_n_corporate_complain.ID_CORPORATE_COMPLAIN'), index=True)
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_corporate_complain = relationship(u'JobNCorporateComplain')


class JobCCorporateInviteInterview(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_invite_interview'

    ID_CORPORATE_INVITE_INTERVIEW = Column(BigInteger, primary_key=True)
    ID_USER_CORPORATE = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_USER_APPLICANT = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    CHOICE_FROM_SEARCH = Column(String(1))
    CHOICE_INTERVIEW = Column(String(1))
    DESCRIPTION = Column(Text)
    DATE_INTERVIEW = Column(Date)
    DATE_INVITE_INTERVIEW = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser', primaryjoin='JobCCorporateInviteInterview.ID_USER_APPLICANT == SysMUser.ID_USER')
    sys_m_user1 = relationship(u'SysMUser', primaryjoin='JobCCorporateInviteInterview.ID_USER_CORPORATE == SysMUser.ID_USER')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCCorporateInviteVacancy(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_invite_vacancy'

    ID_CORPORATE_INVITE_VACANCY = Column(BigInteger, primary_key=True)
    ID_USER_CORPORATE = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_USER_APPLICANT = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    CHOICE_FROM_SEARCH = Column(String(1))
    CHOICE_INVITE_VACANCY = Column(String(1))
    DATE_INVITE_VACANCY = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser', primaryjoin='JobCCorporateInviteVacancy.ID_USER_APPLICANT == SysMUser.ID_USER')
    sys_m_user1 = relationship(u'SysMUser', primaryjoin='JobCCorporateInviteVacancy.ID_USER_CORPORATE == SysMUser.ID_USER')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCCorporateLang(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_lang'

    ID_CORPORATE_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    IMAGE_LOGO_NAME = Column(String(255))
    COMPANY_NAME = Column(String(255))
    FACTORY_NAME = Column(String(255))
    IMAGE_VISION_NAME = Column(String(255))
    NAME_INVOICE = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCorporateProfileLanguage(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_profile_language'

    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), primary_key=True, nullable=False)
    LANG_CODE3 = Column(String(3), primary_key=True, nullable=False)
    IS_DEFAULT_LANGUAGE = Column(String(1))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_c_corporate = relationship(u'JobCCorporate')


class JobCCorporatePurchaseOrder(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_purchase_order'

    ID_CORPORATE_PURCHASE_ORDER = Column(BigInteger, primary_key=True)
    ID_CORPORATE = Column(BigInteger)
    ID_PACKAGE = Column(BigInteger)
    ID_BUDGET = Column(BigInteger)
    ID_ORDER = Column(BigInteger)
    ID_PROMOTION = Column(BigInteger)
    PRICE_TOTAL = Column(Numeric(20, 6))
    QUANTITY = Column(Integer)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCCorporatePurchaseOrderProduct(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_purchase_order_product'

    ID_CORPORATE_PURCHASE_ORDER_PRODUCT = Column(BigInteger, primary_key=True)
    ID_CORPORATE_PURCHASE_ORDER = Column(ForeignKey(u'job_c_corporate_purchase_order.ID_CORPORATE_PURCHASE_ORDER'), index=True)
    ID_PRODUCT_TYPE = Column(BigInteger)
    ID_PRODUCT = Column(BigInteger)
    PRICE = Column(Numeric(20, 6))
    QUANTITY = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_corporate_purchase_order = relationship(u'JobCCorporatePurchaseOrder')


class JobCCorporateRecommendApplicant(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_recommend_applicant'

    ID_APPLICANT_RECOMMEND_VACANCY = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    CHOICE_SEND_FROM = Column(String(1))
    EMAIL_SENDER_RECOMMEND = Column(String(255))
    NAME_RECEIVER_RECOMMEND = Column(String(255))
    EMAIL_RECEIVER_RECOMMEND = Column(String(255))
    DESCRIPTION = Column(Text)
    SEND_DATE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')


class JobCCorporateRecommendApplicantLang(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_recommend_applicant_lang'

    ID_CORPORATE_RECOMMEND_APPLICANT_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE_RECOMMEND_APPLICANT = Column(ForeignKey(u'job_c_corporate_recommend_applicant.ID_APPLICANT_RECOMMEND_VACANCY'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    EMAIL_SENDER_RECOMMEND = Column(String(255))
    EMAIL_RECEIVER_RECOMMEND = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_corporate_recommend_applicant = relationship(u'JobCCorporateRecommendApplicant')


class JobCCorporateTakeTest(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_take_test'

    ID_CORPORATE_TAKE_TEST = Column(BigInteger, primary_key=True)
    ID_BUY_TEST_SCORE = Column(ForeignKey(u'job_m_buy_test_and_score.ID_BUY_TEST_SCORE'), index=True)
    ID_USER_TEST = Column(BigInteger)
    ID_TEST = Column(ForeignKey(u'job_n_test.ID_TEST'), index=True)
    SCORE_TEST = Column(Numeric(20, 2))
    TEST_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    EXPIRE_DATE = Column(Date)
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_m_buy_test_and_score = relationship(u'JobMBuyTestAndScore')
    job_n_test = relationship(u'JobNTest')


class JobCCorporateViewApply(DeclarativeBase2):
    __tablename__ = 'job_c_corporate_view_apply'

    ID_CORPORATE_VIEW_APPLY = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_APPLICANT = Column(ForeignKey(u'job_a_applicant.ID_APPLICANT'), index=True)
    NO_OF_APPLICANT_APPLY = Column(Integer)
    CHOICE_APPLY_FROM = Column(String(1), server_default=text("'A'"))
    CHOICE_RESPONSE_APPLY_STATUS = Column(String(1), server_default=text("'W'"))
    DATE_APPLICANT_APPLY = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_a_applicant = relationship(u'JobAApplicant')
    sys_m_user = relationship(u'SysMUser')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCCorporteInviteTest(DeclarativeBase2):
    __tablename__ = 'job_c_corporte_invite_test'

    ID_CORPORTE_INVITE_TEST = Column(BigInteger, primary_key=True)
    ID_USER_CORPORATE = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_USER_APPLICANT = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_TEST = Column(ForeignKey(u'job_n_test.ID_TEST'), index=True)
    CHOICE_FROM_SEARCH = Column(String(1))
    CHOICE_INVITE_TEST = Column(String(1))
    DATE_INVITE_TEST = Column(Date)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_test = relationship(u'JobNTest')
    sys_m_user = relationship(u'SysMUser', primaryjoin='JobCCorporteInviteTest.ID_USER_APPLICANT == SysMUser.ID_USER')
    sys_m_user1 = relationship(u'SysMUser', primaryjoin='JobCCorporteInviteTest.ID_USER_CORPORATE == SysMUser.ID_USER')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEcEmploymentTask(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_employment_task'

    ID_VA_EC_EMPLOYMENT_TASK = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_EMPLOYMENT_TYPE = Column(ForeignKey(u'job_n_employment_type.ID_EMPLOYMENT_TYPE'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_employment_type = relationship(u'JobNEmploymentType')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEcEtTaskTime(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_et_task_time'

    ID_VA_EC_ET_TASK_TIME = Column(BigInteger, primary_key=True)
    ID_VA_EC_EMPLOYMENT_TASK = Column(ForeignKey(u'job_c_va_ec_employment_task.ID_VA_EC_EMPLOYMENT_TASK'), index=True)
    ID_DAY = Column(ForeignKey(u'job_n_day.ID_DAY'), index=True)
    TIME_START = Column(Time)
    TIME_END = Column(Time)
    TIME_DURATION_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_day = relationship(u'JobNDay')
    job_c_va_ec_employment_task = relationship(u'JobCVaEcEmploymentTask')


class JobCVaEcFringeBenefit(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_fringe_benefit'

    ID_VA_EC_FRINGE_BENEFIT = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_FRINGE_BENEFIT_TYPE = Column(ForeignKey(u'job_n_fringe_benefit_type.ID_FRINGE_BENEFIT_TYPE'), index=True)
    ID_FRINGE_BENEFIT = Column(ForeignKey(u'job_n_fringe_benefit.ID_FRINGE_BENEFIT'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_fringe_benefit = relationship(u'JobNFringeBenefit')
    job_n_fringe_benefit_type = relationship(u'JobNFringeBenefitType')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEcOwnVehicle(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_own_vehicle'

    ID_VA_EC_OWN_VEHICLE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_VEHICLE = Column(ForeignKey(u'job_n_vehicle.ID_VEHICLE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_vacancy = relationship(u'JobCVacancy')
    job_n_vehicle = relationship(u'JobNVehicle')


class JobCVaEcSalaryBase(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_salary_base'

    ID_VA_EC_SALARY_BASE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_SALARY_BASE = Column(ForeignKey(u'job_n_salary_base.ID_SALARY_BASE'), index=True)
    ID_CURRENCY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    CHOICE_WAGES_PER = Column(String(1))
    IS_NEGOTIABLE = Column(String(1))
    SALARY_FROM = Column(Numeric(20, 2))
    SALARY_FROM_USD = Column(Numeric(20, 2))
    SALARY_FROM_USD_RATE = Column(Numeric(20, 6))
    SALARY_TO = Column(Numeric(20, 2))
    SALARY_TO_USD = Column(Numeric(20, 2))
    SALARY_TO_USD_RATE = Column(Numeric(20, 6))
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_currency = relationship(u'JobNCurrency')
    job_n_salary_base = relationship(u'JobNSalaryBase')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEcWorkAbroad(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_work_abroad'

    ID_VA_EC_WORK_ABROAD = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    IS_APPLICANT_WORK_PERMIT = Column(String(1))
    IS_COMPARY_PROVIDE_WORK_PERMIT = Column(String(1))
    WIEGHT_COUNTRY = Column(Integer)
    WEIGHT_PROVINCE = Column(Integer)
    WEIGHT_APPLICANT_WORK_PERMIT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_country = relationship(u'JobNCountry')
    job_n_province = relationship(u'JobNProvince')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEcWorkDomesticLang(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_work_domestic_lang'

    ID_VA_EC_WORK_DEMESTIC_LANG = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    DESCRIPTION = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaEcWorkPlace(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_work_place'

    ID_VA_EC_WORK_PLACE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), nullable=False, index=True)
    CHOICE_WORK_AT = Column(String(1))
    HOUSING_NO = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE = Column(String(255))
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    ID_GPS_TYPE = Column(ForeignKey(u'job_n_gps_type.ID_GPS_TYPE'), index=True)
    LAT = Column(String(255))
    LNG = Column(String(255))
    CLOESED_BY = Column(Text)
    IS_APPLICANT_LOCATED = Column(String(1))
    IS_APPLICANT_WORK_PERMIT = Column(String(1))
    IS_COMPARY_PROVIDE_WORK_PERMIT = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_gps_type = relationship(u'JobNGpsType')
    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_n_province = relationship(u'JobNProvince')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEcWorkPlaceLang(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_work_place_lang'

    ID_VA_EC_WORK_PLACE_LANG = Column(BigInteger, primary_key=True)
    ID_VA_EC_WORK_PLACE = Column(ForeignKey(u'job_c_va_ec_work_place.ID_VA_EC_WORK_PLACE'), index=True)
    ID_VACANCY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    CLOESED_BY = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_va_ec_work_place = relationship(u'JobCVaEcWorkPlace')


class JobCVaEcWpBusRoute(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_wp_bus_route'

    ID_VA_EC_WP_BUS_ROUTE = Column(BigInteger, primary_key=True)
    ID_VA_EC_WORK_PLACE = Column(ForeignKey(u'job_c_va_ec_work_place.ID_VA_EC_WORK_PLACE'), index=True)
    ID_BUS_ROUTE = Column(ForeignKey(u'job_n_bus_route.ID_BUS_ROUTE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_bus_route = relationship(u'JobNBusRoute')
    job_c_va_ec_work_place = relationship(u'JobCVaEcWorkPlace')


class JobCVaEcWpPhone(DeclarativeBase2):
    __tablename__ = 'job_c_va_ec_wp_phone'

    ID_VA_EC_WP_PHONE = Column(BigInteger, primary_key=True)
    ID_VA_EC_WORK_PLACE = Column(ForeignKey(u'job_c_va_ec_work_place.ID_VA_EC_WORK_PLACE'), index=True)
    ID_PHONE_TYPE = Column(BigInteger)
    PHONE_PREFIX = Column(String(255))
    PHONE_NO = Column(String(255))
    PHONE_EXT = Column(String(255))
    TIME_START = Column(Time)
    TIME_END = Column(Time)
    TIME_DURATION_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_va_ec_work_place = relationship(u'JobCVaEcWorkPlace')


class JobCVaEpJobCategory(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_job_category'

    ID_VA_EP_JOB_CATEGORY = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpSaDrivingSkill(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_sa_driving_skill'

    ID_VA_EP_SA_DRIVING_SKILL = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_VEHICLE = Column(ForeignKey(u'job_n_vehicle.ID_VEHICLE'), index=True)
    IS_HAVE_LICENSE = Column(String(1))
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_vacancy = relationship(u'JobCVacancy')
    job_n_vehicle = relationship(u'JobNVehicle')


class JobCVaEpSaHobbieActivitie(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_sa_hobbie_activitie'

    ID_VA_EP_SA_HOBBIE_ACTIVITIE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_HOBBIE_TYPE = Column(ForeignKey(u'job_n_hobbie_type.ID_HOBBIE_TYPE'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_hobbie_type = relationship(u'JobNHobbieType')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpSaOfficeMachineSkill(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_sa_office_machine_skill'

    ID_VA_EP_SA_OFFICE_MACHINE_SKILL = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_OFFICE_MACHINE_SKILL = Column(ForeignKey(u'job_n_office_machine_skill.ID_OFFICE_MACHINE_SKILL'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_office_machine_skill = relationship(u'JobNOfficeMachineSkill')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpSaProfessionalLicense(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_sa_professional_license'

    ID_VA_EP_SA_PROFESSIONAL_LICENSE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_PROFESSIONAL_LICENSE = Column(ForeignKey(u'job_n_professional_license.ID_PROFESSIONAL_LICENSE'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_professional_license = relationship(u'JobNProfessionalLicense')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpSaSpecialSkill(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_sa_special_skill'

    ID_VA_EP_SA_SPECIAL_SKILL = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_JOB_SPECIAL_SKILL = Column(ForeignKey(u'job_n_job_special_skill.ID_JOB_SPECIAL_SKILL'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_special_skill = relationship(u'JobNJobSpecialSkill')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpSaSpecialSkillComputer(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_sa_special_skill_computer'

    ID_VA_EP_SA_SPECIAL_SKILL_COMPUTER = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_SPECIAL_SKILL_COMPUTER_TYPE = Column(ForeignKey(u'job_n_special_skill_computer_type.ID_SPECIAL_SKILL_COMPUTER_TYPE'), index=True)
    ID_SPECIAL_SKILL_COMPUTER = Column(ForeignKey(u'job_n_special_skill_computer.ID_SPECIAL_SKILL_COMPUTER'), index=True)
    ID_PROFICIENCY_SKILL_COMPUTER = Column(ForeignKey(u'job_n_proficiency_skill_computer.ID_PROFICIENCY_SKILL_COMPUTER'), index=True)
    WEIGHT_SPECIAL_SKILL_COMPUTER_TYPE = Column(Integer)
    WEIGHT_SPECIAL_SKILL_COMPUTER = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_proficiency_skill_computer = relationship(u'JobNProficiencySkillComputer')
    job_n_special_skill_computer = relationship(u'JobNSpecialSkillComputer')
    job_n_special_skill_computer_type = relationship(u'JobNSpecialSkillComputerType')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpSaTypingSkill(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_sa_typing_skill'

    ID_VA_EP_SA_TYPING_SKILL = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    WORD_MINUTE = Column(Integer)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_language = relationship(u'JobNLanguage')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpWyBusinessType(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_wy_business_type'

    ID_VA_EP_WY_BUSINESS_TYPE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_BUSINESS_TYPE = Column(ForeignKey(u'job_n_business_type.ID_BUSINESS_TYPE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_business_type = relationship(u'JobNBusinessType')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpWyIndustryCategory(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_wy_industry_category'

    ID_VA_EP_WY_INDUSTRY_CATEGORY = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_INDUSTRY_CATEGORY = Column(ForeignKey(u'job_n_industry_category.ID_INDUSTRY_CATEGORY'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_industry_category = relationship(u'JobNIndustryCategory')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpWyResponsiblePosition(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_wy_responsible_position'

    ID_VA_EP_WY_RESPONSIBLE_POSITION = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_JOB_INDUSTRY = Column(ForeignKey(u'job_n_job_industry.ID_JOB_INDUSTRY'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    ID_JOB_EXPERIENCE = Column(ForeignKey(u'job_n_job_experience.ID_JOB_EXPERIENCE'), index=True)
    TOTAL_YEAR = Column(Integer)
    TOTAL_MONTH = Column(Integer)
    TOTAL_DAY = Column(Integer)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_experience = relationship(u'JobNJobExperience')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    job_n_job_industry = relationship(u'JobNJobIndustry')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaEpWyWorkingExperience(DeclarativeBase2):
    __tablename__ = 'job_c_va_ep_wy_working_experience'

    ID_VA_EP_WY_WORKING_EXPERIENCE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_JOB_INDUSTRY = Column(ForeignKey(u'job_n_job_industry.ID_JOB_INDUSTRY'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    ID_JOB_EXPERIENCE = Column(ForeignKey(u'job_n_job_experience.ID_JOB_EXPERIENCE'), index=True)
    TOTAL_YEAR = Column(Integer)
    TOTAL_MONTH = Column(Integer)
    TOTAL_DAY = Column(Integer)
    NO_YEAR_FROM = Column(Integer)
    NO_YEAR_TO = Column(Integer)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_experience = relationship(u'JobNJobExperience')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    job_n_job_industry = relationship(u'JobNJobIndustry')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPastRecord(DeclarativeBase2):
    __tablename__ = 'job_c_va_past_record'

    ID_VA_PAST_RECORD = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_PERSONAL_PAST_RECORD_ANSWER = Column(ForeignKey(u'job_n_personal_past_record_answer.ID_PERSONAL_PAST_RECORD_ANSWER'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_personal_past_record_answer = relationship(u'JobNPersonalPastRecordAnswer')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPdGender(DeclarativeBase2):
    __tablename__ = 'job_c_va_pd_gender'

    ID_VA_PD_GENDER = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_GENDER = Column(ForeignKey(u'job_n_gender.ID_GENDER'), nullable=False, index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_gender = relationship(u'JobNGender')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPdHandicappedType(DeclarativeBase2):
    __tablename__ = 'job_c_va_pd_handicapped_type'

    ID_VA_PD_HANDICAPPED_TYPE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_HANDICAPPED_TYPE = Column(ForeignKey(u'job_n_handicapped_type.ID_HANDICAPPED_TYPE'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_handicapped_type = relationship(u'JobNHandicappedType')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPdMilitaryStatu(DeclarativeBase2):
    __tablename__ = 'job_c_va_pd_military_status'

    ID_VA_PD_MILITARY_STATUS = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_MILITARY_STATUS = Column(ForeignKey(u'job_n_military_status.ID_MILITARY_STATUS'), nullable=False, index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_military_statu = relationship(u'JobNMilitaryStatu')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPdNationlity(DeclarativeBase2):
    __tablename__ = 'job_c_va_pd_nationlity'

    ID_VA_PD_NATIONLITY = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_NATIONALITY = Column(ForeignKey(u'job_n_nationality.ID_NATIONALITY'), nullable=False, index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_nationality = relationship(u'JobNNationality')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPdRace(DeclarativeBase2):
    __tablename__ = 'job_c_va_pd_race'

    ID_VA_PD_RACE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_RACE = Column(ForeignKey(u'job_n_race.ID_RACE'), nullable=False, index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_race = relationship(u'JobNRace')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPdReligion(DeclarativeBase2):
    __tablename__ = 'job_c_va_pd_religion'

    ID_VA_PD_RELIGION = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_RELIGION = Column(ForeignKey(u'job_n_religion.ID_RELIGION'), nullable=False, index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_religion = relationship(u'JobNReligion')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPqEducation(DeclarativeBase2):
    __tablename__ = 'job_c_va_pq_education'

    ID_VA_PQ_EDUCATION = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_EDUCATION_LEVEL = Column(ForeignKey(u'job_n_education_level.ID_EDUCATION_LEVEL'), index=True)
    ID_DEGREE = Column(ForeignKey(u'job_n_degree.ID_DEGREE'), index=True)
    ID_UNIVERSITY = Column(ForeignKey(u'job_n_university.ID_UNIVERSITY'), index=True)
    ID_FACULTY = Column(ForeignKey(u'job_n_faculty.ID_FACULTY'), index=True)
    ID_FIELD_STUDY = Column(ForeignKey(u'job_n_field_study.ID_FIELD_STUDY'), index=True)
    ID_MAJOR = Column(ForeignKey(u'job_n_major.ID_MAJOR'), index=True)
    GPA_FROM = Column(Numeric(3, 2))
    GPA_TO = Column(Numeric(3, 2))
    IS_INTERNSHIP_EXPERIENCE = Column(String(1))
    WEIGHT_INTERNSHIP_EXPERIENCE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_country = relationship(u'JobNCountry')
    job_n_degree = relationship(u'JobNDegree')
    job_n_education_level = relationship(u'JobNEducationLevel')
    job_n_faculty = relationship(u'JobNFaculty')
    job_n_field_study = relationship(u'JobNFieldStudy')
    job_n_major = relationship(u'JobNMajor')
    job_n_university = relationship(u'JobNUniversity')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPqHonor(DeclarativeBase2):
    __tablename__ = 'job_c_va_pq_honor'

    ID_VA_PQ_HONOR = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_HONOR = Column(ForeignKey(u'job_n_honor.ID_HONOR'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_honor = relationship(u'JobNHonor')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPqLanguageProficiency(DeclarativeBase2):
    __tablename__ = 'job_c_va_pq_language_proficiency'

    ID_VA_PQ_LANGUAGE_PROFICIENCY = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    IS_SPEAKING = Column(String(1))
    IS_READING = Column(String(1))
    IS_LISTENING = Column(String(1))
    IS_WRITING = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_language = relationship(u'JobNLanguage')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPqLanguageStadardizedTest(DeclarativeBase2):
    __tablename__ = 'job_c_va_pq_language_stadardized_test'

    ID_VA_PQ_LANGUAGE_STADARDIZED_TEST = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    ID_LANGUAGE_STANDARDIZED_TEST = Column(ForeignKey(u'job_n_language_standardized_test.ID_LANGUAGE_STANDARDIZED_TEST'), index=True)
    ID_LANGUAGE_STANDARDIZED_TEST_LEVEL = Column(ForeignKey(u'job_n_language_standardized_test_level.ID_LANGUAGE_STANDARDIZED_TEST_LEVEL'), index=True)
    SCORE_TOTAL = Column(Numeric(10, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_language = relationship(u'JobNLanguage')
    job_n_language_standardized_test = relationship(u'JobNLanguageStandardizedTest')
    job_n_language_standardized_test_level = relationship(u'JobNLanguageStandardizedTestLevel')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaPqLpEvaluationCriterion(DeclarativeBase2):
    __tablename__ = 'job_c_va_pq_lp_evaluation_criteria'

    ID_VA_PQ_LP_EVALUATION_CRITERIA = Column(BigInteger, primary_key=True)
    ID_VA_PQ_LANGUAGE_PROFICIENCY = Column(ForeignKey(u'job_c_va_pq_language_proficiency.ID_VA_PQ_LANGUAGE_PROFICIENCY'), index=True)
    CHOICE_TYPE = Column(String(1))
    LEVEL = Column(Enum(u'EXCELLENT', u'GOOD', u'FAIR', u'NOT_EASILY'))
    WEIGHT_EXCELLENT = Column(Integer)
    WEIGHT_GOOD = Column(Integer)
    WEIGHT_FAIR = Column(Integer)
    WEIGHT_NOT_EASILY = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_va_pq_language_proficiency = relationship(u'JobCVaPqLanguageProficiency')


class JobCVaPqPersonalSkill(DeclarativeBase2):
    __tablename__ = 'job_c_va_pq_personal_skill'

    ID_VA_PQ_PERSONAL_SKILL = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_PERSONAL_SKILL_GROUP = Column(ForeignKey(u'job_n_personal_skill_group.ID_PERSONAL_SKILL_GROUP'), index=True)
    ID_PERSONAL_SKILL = Column(ForeignKey(u'job_n_personal_skill.ID_PERSONAL_SKILL'), index=True)
    ID_EVALUATION_PERSONAL_SKILL = Column(ForeignKey(u'job_n_evaluation_personal_skill.ID_EVALUATION_PERSONAL_SKILL'), index=True)
    WIEGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_evaluation_personal_skill = relationship(u'JobNEvaluationPersonalSkill')
    job_n_personal_skill = relationship(u'JobNPersonalSkill')
    job_n_personal_skill_group = relationship(u'JobNPersonalSkillGroup')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaRcContactPerson(DeclarativeBase2):
    __tablename__ = 'job_c_va_rc_contact_person'

    ID_VA_RC_CONTACT_PERSON = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_PREFIX_NAME = Column(ForeignKey(u'job_n_prefix_name.ID_PREFIX_NAME'), index=True)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    POSITION = Column(String(255))
    EMAIL = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_prefix_name = relationship(u'JobNPrefixName')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaRcContactPersonLang(DeclarativeBase2):
    __tablename__ = 'job_c_va_rc_contact_person_lang'

    ID_VA_RC_CONTACT_PERSON_LANG = Column(BigInteger, primary_key=True)
    ID_VA_RC_CONTACT_PERSON = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    POSITION = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaRcCpContactChannel(DeclarativeBase2):
    __tablename__ = 'job_c_va_rc_cp_contact_channel'

    ID_VA_RC_CP_CONTACT_CHANNEL = Column(BigInteger, primary_key=True)
    ID_VA_RC_CONTACT_PERSON = Column(ForeignKey(u'job_c_va_rc_contact_person.ID_VA_RC_CONTACT_PERSON'), index=True)
    ID_SOCIAL_NETWORK = Column(ForeignKey(u'job_n_social_network.ID_SOCIAL_NETWORK'), index=True)
    SOCIAL_PROFILE_ID = Column(String(255))
    SOCIAL_OAUTH_TOKEN = Column(String(255))
    SOCIAL_OAUTH_SECRET_TOKEN = Column(String(255))
    SOCIAL_ACCOUNT_NAME = Column(String(255))
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_social_network = relationship(u'JobNSocialNetwork')
    job_c_va_rc_contact_person = relationship(u'JobCVaRcContactPerson')


class JobCVaRcCpContactChannelLang(DeclarativeBase2):
    __tablename__ = 'job_c_va_rc_cp_contact_channel_lang'

    ID_VA_RC_CP_CONTACT_CHANNEL_LANG = Column(BigInteger, primary_key=True)
    ID_VA_RC_CP_CONTACT_CHANNEL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaRcCpContactPhone(DeclarativeBase2):
    __tablename__ = 'job_c_va_rc_cp_contact_phone'

    ID_VA_RC_CP_CONTACT_PHONE = Column(BigInteger, primary_key=True)
    ID_VA_RC_CONTACT_PERSON = Column(ForeignKey(u'job_c_va_rc_contact_person.ID_VA_RC_CONTACT_PERSON'), index=True)
    ID_PHONE_TYPE = Column(ForeignKey(u'job_n_phone_type.ID_PHONE_TYPE'), index=True)
    PHONE_PREFIX = Column(String(255))
    PHONE_NO = Column(String(255))
    PHONE_EXT = Column(String(255))
    TIME_START = Column(Time)
    TIME_END = Column(Time)
    TIME_DURATION_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_phone_type = relationship(u'JobNPhoneType')
    job_c_va_rc_contact_person = relationship(u'JobCVaRcContactPerson')


class JobCVaRcOtherLanguage(DeclarativeBase2):
    __tablename__ = 'job_c_va_rc_other_language'

    ID_VA_RC_OTHER_LANGUAGE = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_language = relationship(u'JobNLanguage')
    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaWeight(DeclarativeBase2):
    __tablename__ = 'job_c_va_weight'

    ID_VA_WEIGHT = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), index=True)
    NAME = Column(String(255))
    LEVEL = Column(Integer)
    ID_PARENT = Column(BigInteger)
    SEQ = Column(SmallInteger)
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_vacancy = relationship(u'JobCVacancy')


class JobCVaWeightLang(DeclarativeBase2):
    __tablename__ = 'job_c_va_weight_lang'

    ID_VA_WEIGHT_LANG = Column(BigInteger, primary_key=True)
    ID_VA_WEIGHT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVacancy(DeclarativeBase2):
    __tablename__ = 'job_c_vacancy'

    ID_VACANCY = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), index=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_CAREER = Column(ForeignKey(u'job_n_career.ID_CAREER'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    POSITION = Column(String(255))
    NO_POSITION = Column(Integer)
    DATE_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_career = relationship(u'JobNCareer')
    job_c_corporate = relationship(u'JobCCorporate')
    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    sys_m_user = relationship(u'SysMUser')


class JobCVaEmploymentCondition(JobCVacancy):
    __tablename__ = 'job_c_va_employment_condition'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    CHOICE_WORK = Column(String(1))
    IS_HAVE_VEHICLE = Column(String(1))
    IS_START_WORKING = Column(String(1))
    CHOICE_START_WORKING = Column(String(1))
    DATE_START_WORKING = Column(Date)
    CHOICE_SALARY = Column(String(1))
    IS_TRAVELLING = Column(String(1))
    CHOICE_TRAVELLING = Column(String(1))
    CHOICE_TRAVELLING_ON_SITE = Column(String(1))
    WEIGHT_HAVE_VEHICLES = Column(Integer)
    WEIGHT_TRAVELLING = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaRequireCondition(JobCVacancy):
    __tablename__ = 'job_c_va_require_condition'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    IS_APTITUDE_TEST = Column(String(1))
    IS_ATTITUDE_TEST = Column(String(1))
    IS_BMTI_TEST = Column(String(1))
    IS_RESUME_GOT_PHOTO = Column(String(1))
    IS_LANGUAGE_LOCAL = Column(String(1))
    ID_LANGUAGE_LOCAL = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    IS_LANGUAGE_EN = Column(String(1))
    ID_LANGUAGE_EN = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    IS_OTHER_LANGUAGE = Column(String(1))
    WEIGHT_RESUME_GOT_PHOTO = Column(Integer)
    WEIGHT_APTITUDE_TEST = Column(Integer)
    WEIGHT_ATTITUDE_TEST = Column(Integer)
    WEIGHT_BMTI_TEST = Column(Integer)
    WEIGHT_LANGUAGE_LOCAL = Column(Integer)
    WEIGHT_LANGUAGE_EN = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_language = relationship(u'JobNLanguage', primaryjoin='JobCVaRequireCondition.ID_LANGUAGE_EN == JobNLanguage.ID_LANGUAGE')
    job_n_language1 = relationship(u'JobNLanguage', primaryjoin='JobCVaRequireCondition.ID_LANGUAGE_LOCAL == JobNLanguage.ID_LANGUAGE')


class JobCVaExperiencePosition(JobCVacancy):
    __tablename__ = 'job_c_va_experience_position'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    IS_YEAR_EXPERIENCE = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaEpWorkYearExperience(JobCVacancy):
    __tablename__ = 'job_c_va_ep_work_year_experience'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    IS_NEW_GRADUATES = Column(String(1))
    CHOICE_YEAR_EXPERIENCE = Column(String(1))
    NO_YEAR_EXPERIENCE = Column(Integer)
    ID_BUSINESS_TURNOVER = Column(ForeignKey(u'job_n_business_turnover.ID_BUSINESS_TURNOVER'), index=True)
    ID_CURRENCY_BUSINESS_TURNOVER = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    BUSINESS_TURNOVER_MIN_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_MAX_USD = Column(Numeric(20, 2))
    BUSINESS_TURNOVER_RATE = Column(Numeric(20, 2))
    ID_NO_OF_EMPLOYEE = Column(ForeignKey(u'job_n_no_of_employee.ID_NO_OF_EMPLOYEE'), index=True)
    ID_REGISTER_CAPITAL = Column(ForeignKey(u'job_n_register_capital.ID_REGISTER_CAPITAL'), index=True)
    ID_CURRENCY_REGISTER_CAPITAL = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    REGISTER_CAPITAL_MIN_USD = Column(BigInteger)
    REGISTER_CAPITAL_MAX_USD = Column(BigInteger)
    REGISTER_CAPITAL_RATE = Column(BigInteger)
    IS_WORKING_EXPERIENCE = Column(String(1))
    IS_RESPONSIBLE_POSITION = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_business_turnover = relationship(u'JobNBusinessTurnover')
    job_n_currency = relationship(u'JobNCurrency', primaryjoin='JobCVaEpWorkYearExperience.ID_CURRENCY_BUSINESS_TURNOVER == JobNCurrency.ID_CURRENCY')
    job_n_currency1 = relationship(u'JobNCurrency', primaryjoin='JobCVaEpWorkYearExperience.ID_CURRENCY_REGISTER_CAPITAL == JobNCurrency.ID_CURRENCY')
    job_n_no_of_employee = relationship(u'JobNNoOfEmployee')
    job_n_register_capital = relationship(u'JobNRegisterCapital')


class JobCVaEpSkillAbility(JobCVacancy):
    __tablename__ = 'job_c_va_ep_skill_ability'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    SHORTHAND_WORD_MINUTE = Column(Integer)
    IS_HAVE_DRIVING_SKILL = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaPersonalQualification(JobCVacancy):
    __tablename__ = 'job_c_va_personal_qualification'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    IS_HONOR = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaPersonalDatum(JobCVacancy):
    __tablename__ = 'job_c_va_personal_data'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    CHOICE_NATIONALITY = Column(String(1))
    CHOICE_RACE = Column(String(1))
    CHOICE_RELIGION = Column(String(1))
    ID_MARITAL_STATUS = Column(ForeignKey(u'job_n_marital_status.ID_MARITAL_STATUS'), index=True)
    CHOICE_MARITAL_TYPE = Column(String(1))
    AGE_FROM = Column(Integer)
    AGE_TO = Column(Integer)
    WEIGHT_FROM = Column(Integer)
    WEIGHT_TO = Column(Integer)
    ID_WEIGHT_UNIT = Column(ForeignKey(u'job_n_weight_unit.ID_WEIGHT_UNIT'), index=True)
    HEIGHT_FROM = Column(Integer)
    HEIGHT_TO = Column(Integer)
    ID_HEIGHT_UNIT = Column(ForeignKey(u'job_n_height_unit.ID_HEIGHT_UNIT'), index=True)
    IS_HANDICAPPED = Column(String(1))
    FAMILY_SIZE_FROM = Column(Integer)
    FAMILY_SIZE_TO = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_height_unit = relationship(u'JobNHeightUnit')
    job_n_marital_statu = relationship(u'JobNMaritalStatu')
    job_n_weight_unit = relationship(u'JobNWeightUnit')


class JobCVacancyStatistic(JobCVacancy):
    __tablename__ = 'job_c_vacancy_statistic'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True)
    NO_VIEW_VACANCY = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobCVaEcWorkDomestic(JobCVacancy):
    __tablename__ = 'job_c_va_ec_work_domestic'

    ID_VACANCY = Column(ForeignKey(u'job_c_vacancy.ID_VACANCY'), primary_key=True, server_default=text("'0'"))
    CHOICE_WORK_AT = Column(String(1))
    HOUSING_NO = Column(String(255), index=True)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE = Column(String(255))
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    TEL_PREFIX_NO = Column(String(255))
    TEL_NO = Column(String(255))
    TEL_EXT_NO = Column(String(255))
    MOBILE_PREFIX_NO = Column(String(255))
    MOBILE_NO = Column(String(255))
    FAX_PREFIX_NO = Column(String(255))
    FAX_NO = Column(String(255))
    FAX_EXT_NO = Column(String(255))
    ID_GPS_TYPE = Column(ForeignKey(u'job_n_gps_type.ID_GPS_TYPE'), index=True)
    LAT = Column(String(255))
    LNG = Column(String(255))
    CLOESED_BY = Column(Text)
    IS_APPLICANT_LOCATED = Column(String(1))
    WEIGHT_APPLICANT_LOCATED = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_gps_type = relationship(u'JobNGpsType')
    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_n_province = relationship(u'JobNProvince')


class JobCVacancyLang(DeclarativeBase2):
    __tablename__ = 'job_c_vacancy_lang'

    ID_VACANCY_LANG = Column(BigInteger, primary_key=True)
    ID_VACANCY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    POSITION = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMBuyTestAndScore(DeclarativeBase2):
    __tablename__ = 'job_m_buy_test_and_score'

    ID_BUY_TEST_SCORE = Column(BigInteger, primary_key=True)
    ID_JOB_ORDERS = Column(ForeignKey(u'job_m_orders.ID_JOB_ORDERS'), index=True)
    ID_USER_BUYER = Column(BigInteger)
    ID_USER_SELLER = Column(BigInteger)
    CHOICE_USER = Column(String(1))
    CHOICE_PRODUCT_TYPE = Column(String(1))
    ID_TEST = Column(ForeignKey(u'job_n_test.ID_TEST'), index=True)
    SCORE_TEST = Column(Numeric(20, 2))
    QUANTITY = Column(Integer)
    USAGE = Column(Integer)
    ORDERS_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    EXPIRE_DATE = Column(Date)
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_m_order = relationship(u'JobMOrder')
    job_n_test = relationship(u'JobNTest')


class JobMConfigField(DeclarativeBase2):
    __tablename__ = 'job_m_config_field'

    ID_CONFIG_FIELD = Column(BigInteger, primary_key=True)
    ID_PARENT = Column(BigInteger)
    SEQ = Column(Integer)
    PAGE = Column(String(255))
    LABEL = Column(String(255))
    TABLE_NAME = Column(String(255))
    COLUMN_NAME = Column(String(255))
    CHOICE_TYPE_FILED = Column(String(1))
    GUI_NO = Column(String(255))
    GUI_INPUT_NAME = Column(String(255))
    GUI_INPUT_TYPE = Column(String(255))
    GUI_INPUT_RESULT_PAGE = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMConfigFieldDisplay(DeclarativeBase2):
    __tablename__ = 'job_m_config_field_display'

    ID_CONFIG_FIELD_DISPLAY = Column(BigInteger, primary_key=True)
    ID_CONFIG_FIELD = Column(ForeignKey(u'job_m_config_field.ID_CONFIG_FIELD'), index=True)
    ID_ZONE = Column(ForeignKey(u'job_n_zone.ID_ZONE'), index=True)
    ID_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    IS_DISPLAY = Column(String(1, u'utf8_unicode_ci'))
    IS_MANDATORY = Column(String(1, u'utf8_unicode_ci'))
    STATUS = Column(String(1, u'utf8_unicode_ci'), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255, u'utf8_unicode_ci'))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255, u'utf8_unicode_ci'))

    job_m_config_field = relationship(u'JobMConfigField')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    job_n_zone = relationship(u'JobNZone')


class JobMConfigFieldLang(DeclarativeBase2):
    __tablename__ = 'job_m_config_field_lang'

    ID_CONFIG_FIELD_LANG = Column(BigInteger, primary_key=True)
    ID_CONFIG_FIELD = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    PAGE = Column(String(255))
    LABEL = Column(String(255))
    TABLE_NAME = Column(String(255))
    COLUMN_NAME = Column(String(255))
    GUI_INPUT_NAME = Column(String(255))
    GUI_INPUT_TYPE = Column(String(255))
    GUI_INPUT_RESULT_PAGE = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMConfigSegment(DeclarativeBase2):
    __tablename__ = 'job_m_config_segment'

    ID_CONFIG_SEGMENT = Column(BigInteger, primary_key=True)
    SEQ = Column(Integer)
    NAME = Column(String(255, u'utf8_unicode_ci'))
    STATUS = Column(String(1, u'utf8_unicode_ci'), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255, u'utf8_unicode_ci'))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255, u'utf8_unicode_ci'))


class JobMConfigSegmentLang(DeclarativeBase2):
    __tablename__ = 'job_m_config_segment_lang'

    ID_CONFIG_SEGMENT_LANG = Column(BigInteger, primary_key=True)
    ID_CONFIG_SEGMENT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMConfigSegmentMapFiled(DeclarativeBase2):
    __tablename__ = 'job_m_config_segment_map_filed'

    ID_CONFIG_SEGMENT_MAP_FILED = Column(BigInteger, primary_key=True)
    ID_CONFIG_SEGMENT = Column(ForeignKey(u'job_m_config_segment.ID_CONFIG_SEGMENT'), index=True)
    ID_CONFIG_FIELD_DISPLAY_MASTER = Column(ForeignKey(u'job_m_config_field_display.ID_CONFIG_FIELD_DISPLAY'), index=True)
    ID_CONFIG_FIELD_DISPLAY_SLAVE = Column(ForeignKey(u'job_m_config_field_display.ID_CONFIG_FIELD_DISPLAY'), index=True)
    CHOICE_CRITERIA = Column(String(1, u'utf8_unicode_ci'))
    IS_MATCH = Column(String(1, u'utf8_unicode_ci'))
    WEIGHT = Column(Numeric(5, 2))
    STATUS = Column(String(1, u'utf8_unicode_ci'), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255, u'utf8_unicode_ci'))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255, u'utf8_unicode_ci'))

    job_m_config_field_display = relationship(u'JobMConfigFieldDisplay', primaryjoin='JobMConfigSegmentMapFiled.ID_CONFIG_FIELD_DISPLAY_MASTER == JobMConfigFieldDisplay.ID_CONFIG_FIELD_DISPLAY')
    job_m_config_field_display1 = relationship(u'JobMConfigFieldDisplay', primaryjoin='JobMConfigSegmentMapFiled.ID_CONFIG_FIELD_DISPLAY_SLAVE == JobMConfigFieldDisplay.ID_CONFIG_FIELD_DISPLAY')
    job_m_config_segment = relationship(u'JobMConfigSegment')


class JobMContactU(DeclarativeBase2):
    __tablename__ = 'job_m_contact_us'

    ID_CONTACT_US = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger)
    ID_CONTACT_US_TITLE = Column(ForeignKey(u'job_n_contact_us_title.ID_CONTACT_US_TITLE'), index=True)
    NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    EMAIL = Column(String(255))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_n_contact_us_title = relationship(u'JobNContactUsTitle')


class JobMContactUsLang(DeclarativeBase2):
    __tablename__ = 'job_m_contact_us_lang'

    ID_CONTACT_US_LANG = Column(BigInteger, primary_key=True)
    ID_CONTACT_US = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    EMAIL = Column(String(255))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))


class JobMManageWorkingTime(DeclarativeBase2):
    __tablename__ = 'job_m_manage_working_time'

    ID_MANAGE_WORKING_TIME = Column(BigInteger, primary_key=True)
    HOUR_PER_DAY = Column(Integer)
    DAY_PER_WEEK = Column(Integer)
    WEEK_PER_YEAR = Column(Integer)
    ID_COUNTRY = Column(BigInteger)
    DATE_EFFECT_START = Column(Date)
    DATE_EFFECT_EXPIRE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMOrder(DeclarativeBase2):
    __tablename__ = 'job_m_orders'

    ID_JOB_ORDERS = Column(BigInteger, primary_key=True)
    ID_ORDERS = Column(BigInteger)
    COUNTRY_CODE = Column(String(3))
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    CHOICE_USER = Column(String(1))
    ID_CURRENCY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    ORDERS_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    ORDERS_STATUS = Column(String(1))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_n_currency = relationship(u'JobNCurrency')
    sys_m_user = relationship(u'SysMUser')


class JobMRecommentWebsite(DeclarativeBase2):
    __tablename__ = 'job_m_recomment_website'

    ID_RECOMMENT_WEBSITE = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    EMAIL_SENDER = Column(String(255))
    NAME_RECEIVER = Column(String(255))
    EMAIL_RECEIVER = Column(String(255))
    DESCRIPTION = Column(Text)
    SEND_DATE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser')


class JobMRecommentWebsiteLang(DeclarativeBase2):
    __tablename__ = 'job_m_recomment_website_lang'

    ID_RECOMMENT_WEBSITE_LANG = Column(BigInteger, primary_key=True)
    ID_RECOMMENT_WEBSITE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    EMAIL_SENDER = Column(String(255))
    NAME_RECEIVER = Column(String(255))
    EMAIL_RECEIVER = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMUserAddres(DeclarativeBase2):
    __tablename__ = 'job_m_user_address'

    ID_USER_ADDRESS = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_USER_ADDRESS_TYPE = Column(ForeignKey(u'job_n_address_type.ID_ADDRESS_TYPE'), index=True)
    ID_HOUSE_LIVING_CONDITION = Column(ForeignKey(u'job_n_house_living_condition.ID_HOUSE_LIVING_CONDITION'), index=True)
    ID_HOUSE_HOUSING_TYPE = Column(ForeignKey(u'job_n_house_housing_type.ID_HOUSE_HOUSING_TYPE'), index=True)
    ID_HOUSE_PROPERTY_BELONGING = Column(ForeignKey(u'job_n_house_property_belonging.ID_HOUSE_PROPERTY_BELONGING'), index=True)
    RENT_PER_MONTH = Column(Numeric(20, 2))
    ID_CURRENCY_RENT_PER_MONTH = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    RENT_PER_MONTH_USD = Column(Numeric(20, 2))
    RENT_PER_MONTH_USD_RATE = Column(Numeric(20, 6))
    ID_HOUSE_OWNERSHIP = Column(ForeignKey(u'job_n_house_ownership.ID_HOUSE_OWNERSHIP'), index=True)
    NO_LIVING_YEAR = Column(Integer)
    HOUSING_NO = Column(String(255))
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ZIPCODE = Column(String(255))
    ID_INDUSTRY_ESTATE = Column(ForeignKey(u'job_n_industry_estate.ID_INDUSTRY_ESTATE'), index=True)
    TEL_PREFIX_NO = Column(String(255))
    TEL_NO = Column(String(255))
    TEL_EXT_NO = Column(String(255))
    MOBILE_PREFIX_NO = Column(String(255))
    MOBILE_NO = Column(String(255))
    FAX_PREFIX_NO = Column(String(255))
    FAX_NO = Column(String(255))
    FAX_EXT_NO = Column(String(255))
    ID_GPS_TYPE = Column(ForeignKey(u'job_n_gps_type.ID_GPS_TYPE'), index=True)
    LAT = Column(String(255))
    LNG = Column(String(255))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_currency = relationship(u'JobNCurrency')
    job_n_gps_type = relationship(u'JobNGpsType')
    job_n_house_housing_type = relationship(u'JobNHouseHousingType')
    job_n_house_living_condition = relationship(u'JobNHouseLivingCondition')
    job_n_house_ownership = relationship(u'JobNHouseOwnership')
    job_n_house_property_belonging = relationship(u'JobNHousePropertyBelonging')
    job_n_industry_estate = relationship(u'JobNIndustryEstate')
    job_n_province = relationship(u'JobNProvince')
    sys_m_user = relationship(u'SysMUser')
    job_n_address_type = relationship(u'JobNAddressType')


class JobMUserAddressLang(DeclarativeBase2):
    __tablename__ = 'job_m_user_address_lang'

    ID_USER_ADDRESS_LANG = Column(BigInteger, primary_key=True)
    ID_USER_ADDRESS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    STREET_ADDRESS1 = Column(String(255))
    STREET_ADDRESS2 = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMUserEmail(DeclarativeBase2):
    __tablename__ = 'job_m_user_email'

    ID_USER_EMAIL = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    EMAIL = Column(String(255))
    IS_LOGIN = Column(String(1))
    IS_SUBSCRIBE = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser')


class JobMUserImageFace(DeclarativeBase2):
    __tablename__ = 'job_m_user_image_face'

    ID_USER_IMAGE_FACE = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    CHOICE_IMAGE = Column(String(1), index=True)
    IMAGE_NAME = Column(String(255))
    IMAGE_PATH = Column(String(255))
    IMAGE_DESC = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    sys_m_user = relationship(u'SysMUser')


class JobMUserImageFaceLang(DeclarativeBase2):
    __tablename__ = 'job_m_user_image_face_lang'

    ID_USER_IMAGE_FACE_LANG = Column(BigInteger, primary_key=True)
    ID_USER_IMAGE_FACE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    IMAGE_NAME = Column(String(255))
    IMAGE_DESC = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMUserKnowBroadcast(DeclarativeBase2):
    __tablename__ = 'job_m_user_know_broadcast'

    ID_USER_KNOW_BROADCAST = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_BROADCASTING_MEDIA = Column(ForeignKey(u'job_n_broadcasting_media.ID_BROADCASTING_MEDIA'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_broadcasting_media = relationship(u'JobNBroadcastingMedia')
    sys_m_user = relationship(u'SysMUser')


class JobMUserKnowExhibition(DeclarativeBase2):
    __tablename__ = 'job_m_user_know_exhibition'

    ID_USER_KNOW_EXHIBITION = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_EXHIBITION = Column(ForeignKey(u'job_n_exhibition.ID_EXHIBITION'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_exhibition = relationship(u'JobNExhibition')
    sys_m_user = relationship(u'SysMUser')


class JobMUserKnowOnlineMedia(DeclarativeBase2):
    __tablename__ = 'job_m_user_know_online_media'

    ID_USER_KNOW_ONLINE_MEDIA = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_SOCIAL_NETWORK = Column(ForeignKey(u'job_n_social_network.ID_SOCIAL_NETWORK'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_social_network = relationship(u'JobNSocialNetwork')
    sys_m_user = relationship(u'SysMUser')


class JobMUserKnowRecommendIntroduce(DeclarativeBase2):
    __tablename__ = 'job_m_user_know_recommend_introduce'

    ID_USER_KNOW_RECOMMEND_INTRODUCE = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_RECOMMEND_INTRODUCE = Column(ForeignKey(u'job_n_recommend_introduce.ID_RECOMMEND_INTRODUCE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_recommend_introduce = relationship(u'JobNRecommendIntroduce')
    sys_m_user = relationship(u'SysMUser')


class JobMUserPhone(DeclarativeBase2):
    __tablename__ = 'job_m_user_phone'

    ID_USER_PHONE = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_PHONE_TYPE = Column(ForeignKey(u'job_n_phone_type.ID_PHONE_TYPE'), index=True)
    PHONE_PREFIX = Column(String(255))
    PHONE_NO = Column(String(255))
    PHONE_EXT = Column(String(255))
    TIME_START = Column(Time)
    TIME_END = Column(Time)
    TIME_DURATION_MINUTE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_phone_type = relationship(u'JobNPhoneType')
    sys_m_user = relationship(u'SysMUser')


class JobMUserSocialNetwork(DeclarativeBase2):
    __tablename__ = 'job_m_user_social_network'

    ID_USER_SOCIAL_NETWORK = Column(BigInteger, primary_key=True)
    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), index=True)
    ID_SOCIAL_NETWORK = Column(ForeignKey(u'job_n_social_network.ID_SOCIAL_NETWORK'), index=True)
    SOCIAL_PROFILE_ID = Column(String(255))
    SOCIAL_OAUTH_TOKEN = Column(String(255))
    SOCIAL_OAUTH_SECRET_TOKEN = Column(String(400))
    SOCIAL_ACCOUNT_NAME = Column(String(255))
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_social_network = relationship(u'JobNSocialNetwork')
    sys_m_user = relationship(u'SysMUser')


class JobMUserSocialNetworkLang(DeclarativeBase2):
    __tablename__ = 'job_m_user_social_network_lang'

    ID_USER_SOCIAL_NETWORK_LANG = Column(BigInteger, primary_key=True)
    ID_USER_SOCIAL_NETWORK = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    EMAIL_SOCIAL_ACCOUNT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNAddressType(DeclarativeBase2):
    __tablename__ = 'job_n_address_type'

    ID_ADDRESS_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNAddressTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_address_type_lang'

    ID_ADDRESS_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_ADDRESS_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantAddressType(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_address_type'

    ID_APPLICANT_ADDRESS_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantAddressTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_address_type_lang'

    ID_APPLICANT_ADDRESS_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_ADDRESS_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantCertificateType(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_certificate_type'

    ID_APPLICANT_CERTIFICATE_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantCertificateTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_certificate_type_lang'

    ID_APPLICANT_CERTIFICATE_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_CERTIFICATE_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantComplain(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_complain'

    ID_APPLICANT_COMPLAIN = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantComplainLang(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_complain_lang'

    ID_APPLICANT_COMPLAIN_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_COMPLAIN = Column(ForeignKey(u'job_n_applicant_complain.ID_APPLICANT_COMPLAIN'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_applicant_complain = relationship(u'JobNApplicantComplain')


class JobNApplicantFamilyType(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_family_type'

    ID_APPLICANT_FAMILY_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantFamilyTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_family_type_lang'

    ID_APPLICANT_FAMILY_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_FAMILY_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantImageType(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_image_type'

    ID_APPLICANT_IMAGE_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNApplicantImageTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_applicant_image_type_lang'

    ID_APPLICANT_IMAGE_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_APPLICANT_IMAGE_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBloodGroup(DeclarativeBase2):
    __tablename__ = 'job_n_blood_group'

    ID_BLOOD_GROUP = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBloodGroupLang(DeclarativeBase2):
    __tablename__ = 'job_n_blood_group_lang'

    ID_BLOOD_GROUP_LANG = Column(BigInteger, primary_key=True)
    ID_BLOOD_GROUP = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBroadcastingMedia(DeclarativeBase2):
    __tablename__ = 'job_n_broadcasting_media'

    ID_BROADCASTING_MEDIA = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBroadcastingMediaLang(DeclarativeBase2):
    __tablename__ = 'job_n_broadcasting_media_lang'

    ID_BROADCASTING_MEDIA_LANG = Column(BigInteger, primary_key=True)
    ID_BROADCASTING_MEDIA = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBusRoute(DeclarativeBase2):
    __tablename__ = 'job_n_bus_route'

    ID_BUS_ROUTE = Column(BigInteger, primary_key=True)
    ID_COUNTRY = Column(BigInteger, index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_county = relationship(u'JobNCounty')
    job_n_country = relationship(u'JobNCountry')
    job_n_province = relationship(u'JobNProvince')


class JobNBusRouteLang(DeclarativeBase2):
    __tablename__ = 'job_n_bus_route_lang'

    ID_BUS_ROUTE_LANG = Column(BigInteger, primary_key=True)
    ID_BUS_ROUTE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBusinessTurnover(DeclarativeBase2):
    __tablename__ = 'job_n_business_turnover'

    ID_BUSINESS_TURNOVER = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    MIN = Column(Numeric(20, 2))
    MAX = Column(Numeric(20, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBusinessTurnoverLang(DeclarativeBase2):
    __tablename__ = 'job_n_business_turnover_lang'

    ID_BUSINESS_TURNOVER_LANG = Column(BigInteger, primary_key=True)
    ID_BUSINESS_TURNOVER = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBusinessType(DeclarativeBase2):
    __tablename__ = 'job_n_business_type'

    ID_BUSINESS_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNBusinessTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_business_type_lang'

    ID_BUSINESS_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_BUSINESS_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCareer(DeclarativeBase2):
    __tablename__ = 'job_n_career'

    ID_CAREER = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCareerLang(DeclarativeBase2):
    __tablename__ = 'job_n_career_lang'

    ID_CAREER_LANG = Column(BigInteger, primary_key=True)
    ID_CAREER = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCity(DeclarativeBase2):
    __tablename__ = 'job_n_city'

    ID_CITY = Column(BigInteger, primary_key=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_province = relationship(u'JobNProvince')


class JobNCityLang(DeclarativeBase2):
    __tablename__ = 'job_n_city_lang'

    ID_CITY_LANG = Column(BigInteger, primary_key=True)
    ID_CITY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCommuterStation(DeclarativeBase2):
    __tablename__ = 'job_n_commuter_station'

    ID_COMMUTER_STATION = Column(BigInteger, primary_key=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_county = relationship(u'JobNCounty')


class JobNCommuterStationLang(DeclarativeBase2):
    __tablename__ = 'job_n_commuter_station_lang'

    ID_COMMUTER_STATION_LANG = Column(BigInteger, primary_key=True)
    ID_COMMUTER_STATION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNComplexion(DeclarativeBase2):
    __tablename__ = 'job_n_complexion'

    ID_COMPLEXION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNComplexionLang(DeclarativeBase2):
    __tablename__ = 'job_n_complexion_lang'

    ID_COMPLEXION_LANG = Column(BigInteger, primary_key=True)
    ID_COMPLEXION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNConsumerProduct(DeclarativeBase2):
    __tablename__ = 'job_n_consumer_product'

    ID_CONSUMER_PRODUCT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNConsumerProductLang(DeclarativeBase2):
    __tablename__ = 'job_n_consumer_product_lang'

    ID_CONSUMER_PRODUCT_LANG = Column(BigInteger, primary_key=True)
    ID_CONSUMER_PRODUCT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNContactUsTitle(DeclarativeBase2):
    __tablename__ = 'job_n_contact_us_title'

    ID_CONTACT_US_TITLE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))


class JobNContactUsTitleLang(DeclarativeBase2):
    __tablename__ = 'job_n_contact_us_title_lang'

    ID_CONTACT_US_TITLE_LANG = Column(BigInteger, primary_key=True)
    ID_CONTACT_US_TITLE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))


class JobNCorporateAddressType(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_address_type'

    ID_CORPORATE_ADDRESS_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCorporateAddressTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_address_type_lang'

    ID_CORPORATE_ADDRESS_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE_ADDRESS_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCorporateCertificateType(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_certificate_type'

    ID_CORPORATE_CERTIFICATE_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCorporateCertificateTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_certificate_type_lang'

    ID_CORPORATE_CERTIFICATE_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE_CERTIFICATE_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCorporateComplain(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_complain'

    ID_CORPORATE_COMPLAIN = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCorporateComplainLang(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_complain_lang'

    ID_CORPORATE_COMPLAIN_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE_COMPLAIN = Column(ForeignKey(u'job_n_corporate_complain.ID_CORPORATE_COMPLAIN'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_corporate_complain = relationship(u'JobNCorporateComplain')


class JobNCorporateSize(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_size'

    ID_CORPORATE_SIZE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCorporateSizeLang(DeclarativeBase2):
    __tablename__ = 'job_n_corporate_size_lang'

    ID_CORPORATE_SIZE_LANG = Column(BigInteger, primary_key=True)
    ID_CORPORATE_SIZE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCountry(DeclarativeBase2):
    __tablename__ = 'job_n_country'

    ID_COUNTRY = Column(BigInteger, primary_key=True)
    ID_REGION = Column(ForeignKey(u'job_n_region.ID_REGION'), index=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    ID_CURRENCY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    PHONE_CODE = Column(String(10))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_currency = relationship(u'JobNCurrency')
    job_n_language = relationship(u'JobNLanguage')
    job_n_region = relationship(u'JobNRegion')


class JobNCountryLang(DeclarativeBase2):
    __tablename__ = 'job_n_country_lang'

    ID_COUNTRY_LANG = Column(BigInteger, primary_key=True)
    ID_COUNTRY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCounty(DeclarativeBase2):
    __tablename__ = 'job_n_county'

    ID_COUNTY = Column(BigInteger, primary_key=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')


class JobNCountyLang(DeclarativeBase2):
    __tablename__ = 'job_n_county_lang'

    ID_COUNTY_LANG = Column(BigInteger, primary_key=True)
    ID_COUNTY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCountyMapZipcode(DeclarativeBase2):
    __tablename__ = 'job_n_county_map_zipcode'

    ID_COUNTY_MAP_ZIPCODE = Column(BigInteger, primary_key=True, index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    ID_ZIPCODE = Column(ForeignKey(u'job_n_zipcode.ID_ZIPCODE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_county = relationship(u'JobNCounty')
    job_n_zipcode = relationship(u'JobNZipcode')


class JobNCurrency(DeclarativeBase2):
    __tablename__ = 'job_n_currency'

    ID_CURRENCY = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCurrencyLang(DeclarativeBase2):
    __tablename__ = 'job_n_currency_lang'

    ID_CURRENCY_LANG = Column(BigInteger, primary_key=True)
    ID_CURRENCY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCurrentEmploymentStatu(DeclarativeBase2):
    __tablename__ = 'job_n_current_employment_status'

    ID_CURRENT_EMPLOYMENT_STATUS = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNCurrentEmploymentStatusLang(DeclarativeBase2):
    __tablename__ = 'job_n_current_employment_status_lang'

    ID_CURRENT_EMPLOYMENT_STATUS_LANG = Column(BigInteger, primary_key=True)
    ID_CURRENT_EMPLOYMENT_STATUS = Column(ForeignKey(u'job_n_current_employment_status.ID_CURRENT_EMPLOYMENT_STATUS'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_current_employment_statu = relationship(u'JobNCurrentEmploymentStatu')


class JobNDay(DeclarativeBase2):
    __tablename__ = 'job_n_day'

    ID_DAY = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDayLang(DeclarativeBase2):
    __tablename__ = 'job_n_day_lang'

    ID_DAY_LANG = Column(BigInteger, primary_key=True)
    ID_DAY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDegree(DeclarativeBase2):
    __tablename__ = 'job_n_degree'

    ID_DEGREE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDegreeLang(DeclarativeBase2):
    __tablename__ = 'job_n_degree_lang'

    ID_DEGREE_LANG = Column(BigInteger, primary_key=True)
    ID_DEGREE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDisease(DeclarativeBase2):
    __tablename__ = 'job_n_diseases'

    ID_DISEASES = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDiseasesLang(DeclarativeBase2):
    __tablename__ = 'job_n_diseases_lang'

    ID_DISEASES_LANG = Column(BigInteger, primary_key=True)
    ID_DISEASES = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDrivingSkill(DeclarativeBase2):
    __tablename__ = 'job_n_driving_skill'

    ID_DRIVING_SKILL = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDrivingSkillLang(DeclarativeBase2):
    __tablename__ = 'job_n_driving_skill_lang'

    ID_DRIVING_SKILL_LANG = Column(BigInteger, primary_key=True)
    ID_DRIVING_SKILL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNDuringUnemployed(DeclarativeBase2):
    __tablename__ = 'job_n_during_unemployed'

    ID_DURING_UNEMPLOYED = Column(BigInteger, primary_key=True)
    ID_CURRENT_EMPLOYMENT_STATUS = Column(ForeignKey(u'job_n_current_employment_status.ID_CURRENT_EMPLOYMENT_STATUS'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_current_employment_statu = relationship(u'JobNCurrentEmploymentStatu')


class JobNDuringUnemployedLang(DeclarativeBase2):
    __tablename__ = 'job_n_during_unemployed_lang'

    ID_DURING_UNEMPLOYED_LANG = Column(BigInteger, primary_key=True)
    ID_DURING_UNEMPLOYED = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEducationLevel(DeclarativeBase2):
    __tablename__ = 'job_n_education_level'

    ID_EDUCATION_LEVEL = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEducationLevelLang(DeclarativeBase2):
    __tablename__ = 'job_n_education_level_lang'

    ID_EDUCATION_LEVEL_LANG = Column(BigInteger, primary_key=True)
    ID_EDUCATION_LEVEL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEmpStatu(DeclarativeBase2):
    __tablename__ = 'job_n_emp_status'

    ID_EMP_STATUS = Column(BigInteger, primary_key=True)
    ID_EMP_STATUS_TYPE = Column(ForeignKey(u'job_n_emp_status_type.ID_EMP_STATUS_TYPE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_emp_status_type = relationship(u'JobNEmpStatusType')


class JobNEmpStatusLang(DeclarativeBase2):
    __tablename__ = 'job_n_emp_status_lang'

    ID_EMP_STATUS_LANG = Column(BigInteger, primary_key=True)
    ID_EMP_STATUS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEmpStatusType(DeclarativeBase2):
    __tablename__ = 'job_n_emp_status_type'

    ID_EMP_STATUS_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEmpStatusTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_emp_status_type_lang'

    ID_EMP_STATUS_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_EMP_STATUS_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEmploymentType(DeclarativeBase2):
    __tablename__ = 'job_n_employment_type'

    ID_EMPLOYMENT_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEmploymentTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_employment_type_lang'

    ID_EMPLOYMENT_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_EMPLOYMENT_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEndProduct(DeclarativeBase2):
    __tablename__ = 'job_n_end_product'

    ID_END_PRODUCT = Column(BigInteger, primary_key=True)
    ID_END_PRODUCT_TYPE = Column(ForeignKey(u'job_n_end_product_type.ID_END_PRODUCT_TYPE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_end_product_type = relationship(u'JobNEndProductType')


class JobNEndProductLang(DeclarativeBase2):
    __tablename__ = 'job_n_end_product_lang'

    ID_END_PRODUCT_LANG = Column(BigInteger, primary_key=True)
    ID_END_PRODUCT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEndProductType(DeclarativeBase2):
    __tablename__ = 'job_n_end_product_type'

    ID_END_PRODUCT_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEndProductTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_end_product_type_lang'

    ID_END_PRODUCT_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_END_PRODUCT_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEntreprenerType(DeclarativeBase2):
    __tablename__ = 'job_n_entreprener_type'

    ID_ENTREPRENER_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEntreprenerTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_entreprener_type_lang'

    ID_ENTREPRENER_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_ENTREPRENER_TYPE = Column(ForeignKey(u'job_n_entreprener_type.ID_ENTREPRENER_TYPE'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_entreprener_type = relationship(u'JobNEntreprenerType')


class JobNEvaluationLanguage(DeclarativeBase2):
    __tablename__ = 'job_n_evaluation_language'

    ID_EVALUATION_LANGUAGE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEvaluationLanguageLang(DeclarativeBase2):
    __tablename__ = 'job_n_evaluation_language_lang'

    ID_EVALUATION_LANGUAGE_LANG = Column(BigInteger, primary_key=True)
    ID_EVALUATION_LANGUAGE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEvaluationPersonalSkill(DeclarativeBase2):
    __tablename__ = 'job_n_evaluation_personal_skill'

    ID_EVALUATION_PERSONAL_SKILL = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    SCORE = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEvaluationPersonalSkillLang(DeclarativeBase2):
    __tablename__ = 'job_n_evaluation_personal_skill_lang'

    ID_EVALUATION_PERSONAL_SKILL_LANG = Column(BigInteger, primary_key=True)
    ID_EVALUATION_PERSONAL_SKILL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEveluationTopic(DeclarativeBase2):
    __tablename__ = 'job_n_eveluation_topic'

    ID_EVELUATION_TOPIC = Column(BigInteger, primary_key=True)
    ID_PERSONAL_SKILL = Column(ForeignKey(u'job_n_personal_skill.ID_PERSONAL_SKILL'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_personal_skill = relationship(u'JobNPersonalSkill')


class JobNEveluationTopicLang(DeclarativeBase2):
    __tablename__ = 'job_n_eveluation_topic_lang'

    ID_EVELUATION_TOPIC_LANG = Column(BigInteger, primary_key=True)
    ID_EVELUATION_TOPIC = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNExhibition(DeclarativeBase2):
    __tablename__ = 'job_n_exhibition'

    ID_EXHIBITION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNExhibitionLang(DeclarativeBase2):
    __tablename__ = 'job_n_exhibition_lang'

    ID_EXHIBITION_LANG = Column(BigInteger, primary_key=True)
    ID_EXHIBITION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEyeColor(DeclarativeBase2):
    __tablename__ = 'job_n_eye_color'

    ID_EYE_COLOR = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNEyeColorLang(DeclarativeBase2):
    __tablename__ = 'job_n_eye_color_lang'

    ID_EYE_COLOR_LANG = Column(BigInteger, primary_key=True)
    ID_EYE_COLOR = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFaculty(DeclarativeBase2):
    __tablename__ = 'job_n_faculty'

    ID_FACULTY = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFacultyLang(DeclarativeBase2):
    __tablename__ = 'job_n_faculty_lang'

    ID_FACULTY_LANG = Column(BigInteger, primary_key=True)
    ID_FACULTY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFamilySize(DeclarativeBase2):
    __tablename__ = 'job_n_family_size'

    ID_FAMILY_SIZE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFamilySizeLang(DeclarativeBase2):
    __tablename__ = 'job_n_family_size_lang'

    ID_FAMILY_SIZE_LANG = Column(BigInteger, primary_key=True)
    ID_FAMILY_SIZE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFieldStudy(DeclarativeBase2):
    __tablename__ = 'job_n_field_study'

    ID_FIELD_STUDY = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFieldStudyLang(DeclarativeBase2):
    __tablename__ = 'job_n_field_study_lang'

    ID_FIELD_STUDY_LANG = Column(BigInteger, primary_key=True)
    ID_FIELD_STUDY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFringeBenefit(DeclarativeBase2):
    __tablename__ = 'job_n_fringe_benefit'

    ID_FRINGE_BENEFIT = Column(BigInteger, primary_key=True)
    ID_FRINGE_BENEFIT_TYPE = Column(ForeignKey(u'job_n_fringe_benefit_type.ID_FRINGE_BENEFIT_TYPE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    IS_TAX = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_fringe_benefit_type = relationship(u'JobNFringeBenefitType')


class JobNFringeBenefitLang(DeclarativeBase2):
    __tablename__ = 'job_n_fringe_benefit_lang'

    ID_FRINGE_BENEFIT_LANG = Column(BigInteger, primary_key=True)
    ID_FRINGE_BENEFIT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFringeBenefitType(DeclarativeBase2):
    __tablename__ = 'job_n_fringe_benefit_type'

    ID_FRINGE_BENEFIT_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNFringeBenefitTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_fringe_benefit_type_lang'

    ID_FRINGE_BENEFIT_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_FRINGE_BENEFIT_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGenPersonalTest(DeclarativeBase2):
    __tablename__ = 'job_n_gen_personal_test'

    ID_GEN_PERSONAL_TEST = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGenPersonalTestLang(DeclarativeBase2):
    __tablename__ = 'job_n_gen_personal_test_lang'

    ID_GEN_PERSONAL_TEST_LANG = Column(BigInteger, primary_key=True)
    ID_GEN_PERSONAL_TEST = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGender(DeclarativeBase2):
    __tablename__ = 'job_n_gender'

    ID_GENDER = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGenderLang(DeclarativeBase2):
    __tablename__ = 'job_n_gender_lang'

    ID_GENDER_LANG = Column(BigInteger, primary_key=True)
    ID_GENDER = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGpa(DeclarativeBase2):
    __tablename__ = 'job_n_gpa'

    ID_GPA = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGpaLang(DeclarativeBase2):
    __tablename__ = 'job_n_gpa_lang'

    ID_GPA_LANG = Column(BigInteger, primary_key=True)
    ID_GPA = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGpsType(DeclarativeBase2):
    __tablename__ = 'job_n_gps_type'

    ID_GPS_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNGpsTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_gps_type_lang'

    ID_GPS_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_GPS_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHandicappedType(DeclarativeBase2):
    __tablename__ = 'job_n_handicapped_type'

    ID_HANDICAPPED_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHandicappedTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_handicapped_type_lang'

    ID_HANDICAPPED_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_HANDICAPPED_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHealthAnswer(DeclarativeBase2):
    __tablename__ = 'job_n_health_answer'

    ID_HEALTH_ANSWER = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    ID_HEALTH_ANSWER_TYPE = Column(ForeignKey(u'job_n_health_answer_type.ID_HEALTH_ANSWER_TYPE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_health_answer_type = relationship(u'JobNHealthAnswerType')


class JobNHealthAnswerType(DeclarativeBase2):
    __tablename__ = 'job_n_health_answer_type'

    ID_HEALTH_ANSWER_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHealthQuestion(DeclarativeBase2):
    __tablename__ = 'job_n_health_question'

    ID_HEALTH_QUESTION = Column(BigInteger, primary_key=True)
    ID_HEALTH_QUESTION_GROUP = Column(ForeignKey(u'job_n_health_question_group.ID_HEALTH_QUESTION_GROUP'), index=True)
    ID_PARENT = Column(BigInteger)
    LEVEL = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    SEQ = Column(SmallInteger)
    NAME = Column(Text)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_health_question_group = relationship(u'JobNHealthQuestionGroup')


class JobNHealthQuestionAnswer(DeclarativeBase2):
    __tablename__ = 'job_n_health_question_answer'

    ID_HEALTH_QUESTION_ANSWER = Column(BigInteger, primary_key=True)
    ID_HEALTH_QUESTION = Column(ForeignKey(u'job_n_health_question.ID_HEALTH_QUESTION'), index=True)
    ID_HEALTH_ANSWER = Column(ForeignKey(u'job_n_health_answer.ID_HEALTH_ANSWER'), index=True)
    ID_PARENT = Column(BigInteger)
    LEVEL = Column(Integer)
    SEQ = Column(SmallInteger)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_health_answer = relationship(u'JobNHealthAnswer')
    job_n_health_question = relationship(u'JobNHealthQuestion')


class JobNHealthQuestionGroup(DeclarativeBase2):
    __tablename__ = 'job_n_health_question_group'

    ID_HEALTH_QUESTION_GROUP = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHeightUnit(DeclarativeBase2):
    __tablename__ = 'job_n_height_unit'

    ID_HEIGHT_UNIT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHeightUnitLang(DeclarativeBase2):
    __tablename__ = 'job_n_height_unit_lang'

    ID_HEIGHT_UNIT_LANG = Column(BigInteger, primary_key=True)
    ID_HEIGHT_UNIT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHobbie(DeclarativeBase2):
    __tablename__ = 'job_n_hobbie'

    ID_HOBBIE = Column(BigInteger, primary_key=True)
    ID_HOBBIE_TYPE = Column(ForeignKey(u'job_n_hobbie_type.ID_HOBBIE_TYPE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_hobbie_type = relationship(u'JobNHobbieType')


class JobNHobbieLang(DeclarativeBase2):
    __tablename__ = 'job_n_hobbie_lang'

    ID_HOBBIE_LANG = Column(BigInteger, primary_key=True)
    ID_HOBBIE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHobbieType(DeclarativeBase2):
    __tablename__ = 'job_n_hobbie_type'

    ID_HOBBIE_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHobbieTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_hobbie_type_lang'

    ID_HOBBIE_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_HOBBIE_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHonor(DeclarativeBase2):
    __tablename__ = 'job_n_honor'

    ID_HONOR = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHonorLang(DeclarativeBase2):
    __tablename__ = 'job_n_honor_lang'

    ID_HONOR_LANG = Column(BigInteger, primary_key=True)
    ID_HONOR = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHouseHousingType(DeclarativeBase2):
    __tablename__ = 'job_n_house_housing_type'

    ID_HOUSE_HOUSING_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHouseHousingTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_house_housing_type_lang'

    ID_HOUSE_HOUSING_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_HOUSE_HOUSING_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHouseLivingCondition(DeclarativeBase2):
    __tablename__ = 'job_n_house_living_condition'

    ID_HOUSE_LIVING_CONDITION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHouseLivingConditionLang(DeclarativeBase2):
    __tablename__ = 'job_n_house_living_condition_lang'

    ID_HOUSE_LIVING_CONDITION_LANG = Column(BigInteger, primary_key=True)
    ID_HOUSE_LIVING_CONDITION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHouseOwnership(DeclarativeBase2):
    __tablename__ = 'job_n_house_ownership'

    ID_HOUSE_OWNERSHIP = Column(BigInteger, primary_key=True)
    ID_HOUSE_PROPERTY_BELONGING = Column(ForeignKey(u'job_n_house_property_belonging.ID_HOUSE_PROPERTY_BELONGING'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_house_property_belonging = relationship(u'JobNHousePropertyBelonging')


class JobNHouseOwnershipLang(DeclarativeBase2):
    __tablename__ = 'job_n_house_ownership_lang'

    ID_HOUSE_OWNERSHIP_LANG = Column(BigInteger, primary_key=True)
    ID_HOUSE_OWNERSHIP = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHousePropertyBelonging(DeclarativeBase2):
    __tablename__ = 'job_n_house_property_belonging'

    ID_HOUSE_PROPERTY_BELONGING = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNHousePropertyBelongingLang(DeclarativeBase2):
    __tablename__ = 'job_n_house_property_belonging_lang'

    ID_HOUSE_PROPERTY_BELONGING_LANG = Column(BigInteger, primary_key=True)
    ID_HOUSE_PROPERTY_BELONGING = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIncomeBase(DeclarativeBase2):
    __tablename__ = 'job_n_income_base'

    ID_INCOME_BASE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIncomeBaseLang(DeclarativeBase2):
    __tablename__ = 'job_n_income_base_lang'

    ID_INCOME_BASE_LANG = Column(BigInteger, primary_key=True)
    ID_INCOME_BASE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIncomeTaxPayment(DeclarativeBase2):
    __tablename__ = 'job_n_income_tax_payment'

    ID_INCOME_TAX_PAYMENT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIncomeTaxPaymentLang(DeclarativeBase2):
    __tablename__ = 'job_n_income_tax_payment_lang'

    ID_INCOME_TAX_PAYMENT_LANG = Column(BigInteger, primary_key=True)
    ID_INCOME_TAX_PAYMENT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIndustrialProduct(DeclarativeBase2):
    __tablename__ = 'job_n_industrial_product'

    ID_INDUSTRIAL_PRODUCT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIndustrialProductLang(DeclarativeBase2):
    __tablename__ = 'job_n_industrial_product_lang'

    ID_INDUSTRIAL_PRODUCT_LANG = Column(BigInteger, primary_key=True)
    ID_INDUSTRIAL_PRODUCT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIndustry(DeclarativeBase2):
    __tablename__ = 'job_n_industry'

    ID_INDUSTRY = Column(BigInteger, primary_key=True)
    ID_INDUSTRY_CATEGORY = Column(ForeignKey(u'job_n_industry_category.ID_INDUSTRY_CATEGORY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_industry_category = relationship(u'JobNIndustryCategory')


class JobNIndustryCategory(DeclarativeBase2):
    __tablename__ = 'job_n_industry_category'

    ID_INDUSTRY_CATEGORY = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIndustryCategoryLang(DeclarativeBase2):
    __tablename__ = 'job_n_industry_category_lang'

    ID_INDUSTRY_CATEGORY_LANG = Column(BigInteger, primary_key=True)
    ID_INDUSTRY_CATEGORY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIndustryEstate(DeclarativeBase2):
    __tablename__ = 'job_n_industry_estate'

    ID_INDUSTRY_ESTATE = Column(BigInteger, primary_key=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_province = relationship(u'JobNProvince')


class JobNIndustryEstateLang(DeclarativeBase2):
    __tablename__ = 'job_n_industry_estate_lang'

    ID_INDUSTRY_ESTATE_LANG = Column(BigInteger, primary_key=True)
    ID_INDUSTRY_ESTATE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIndustryLang(DeclarativeBase2):
    __tablename__ = 'job_n_industry_lang'

    ID_INDUSTRY_LANG = Column(BigInteger, primary_key=True)
    ID_INDUSTRY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNIpGeo(DeclarativeBase2):
    __tablename__ = 'job_n_ip_geo'

    ID_IP_GEO = Column(BigInteger, primary_key=True)
    IP_START = Column(BigInteger, nullable=False)
    IP_END = Column(BigInteger, nullable=False)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_province = relationship(u'JobNProvince')


class JobNJobCategory(DeclarativeBase2):
    __tablename__ = 'job_n_job_category'

    ID_JOB_CATEGORY = Column(BigInteger, primary_key=True)
    ID_PARENT = Column(ForeignKey(u'job_n_job_category.ID_JOB_CATEGORY'), index=True)
    LEVEL = Column(Integer)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    parent = relationship(u'JobNJobCategory', remote_side=[ID_JOB_CATEGORY])


class JobNJobCategoryLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_category_lang'

    ID_JOB_CATEGORY_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_CATEGORY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobCategoryMapJobExperience(DeclarativeBase2):
    __tablename__ = 'job_n_job_category_map_job_experience'

    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), primary_key=True, nullable=False)
    ID_JOB_EXPERIENCE = Column(ForeignKey(u'job_n_job_experience.ID_JOB_EXPERIENCE'), primary_key=True, nullable=False, index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_experience = relationship(u'JobNJobExperience')


class JobNJobDivision(DeclarativeBase2):
    __tablename__ = 'job_n_job_division'

    ID_JOB_DIVISION = Column(BigInteger, primary_key=True)
    ID_PARENT = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    LEVEL = Column(SmallInteger)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    parent = relationship(u'JobNJobDivision', remote_side=[ID_JOB_DIVISION])


class JobNJobDivisionLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_division_lang'

    ID_JOB_DIVISION_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_DIVISION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobExperience(DeclarativeBase2):
    __tablename__ = 'job_n_job_experience'

    ID_JOB_EXPERIENCE = Column(BigInteger, primary_key=True)
    ID_JOB_HIERARCHY_GROUP = Column(ForeignKey(u'job_n_job_hierarchy_group.ID_JOB_HIERARCHY_GROUP'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    job_n_job_hierarchy_group = relationship(u'JobNJobHierarchyGroup')


class JobNJobExperienceLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_experience_lang'

    ID_JOB_EXPERIENCE_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_EXPERIENCE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobHierarchy(DeclarativeBase2):
    __tablename__ = 'job_n_job_hierarchy'

    ID_JOB_HIERARCHY = Column(BigInteger, primary_key=True)
    ID_JOB_HIERARCHY_GROUP = Column(ForeignKey(u'job_n_job_hierarchy_group.ID_JOB_HIERARCHY_GROUP'), index=True)
    SEQ = Column(SmallInteger)
    PRIORITY = Column(Integer)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_hierarchy_group = relationship(u'JobNJobHierarchyGroup')


class JobNJobHierarchyGroup(DeclarativeBase2):
    __tablename__ = 'job_n_job_hierarchy_group'

    ID_JOB_HIERARCHY_GROUP = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobHierarchyGroupLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_hierarchy_group_lang'

    ID_JOB_HIERARCHY_GROUP_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_HIERARCHY_GROUP = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobHierarchyLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_hierarchy_lang'

    ID_JOB_HIERARCHY_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_HIERARCHY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobIndustry(DeclarativeBase2):
    __tablename__ = 'job_n_job_industry'

    ID_JOB_INDUSTRY = Column(BigInteger, primary_key=True)
    ID_PARENT = Column(ForeignKey(u'job_n_job_industry.ID_JOB_INDUSTRY'), index=True)
    LEVEL = Column(SmallInteger)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    parent = relationship(u'JobNJobIndustry', remote_side=[ID_JOB_INDUSTRY])


class JobNJobIndustryLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_industry_lang'

    ID_JOB_INDUSTRY_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_INDUSTRY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobPosition(DeclarativeBase2):
    __tablename__ = 'job_n_job_position'

    ID_JOB_POSITION = Column(BigInteger, primary_key=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision', primaryjoin='JobNJobPosition.ID_JOB_DIVISION == JobNJobDivision.ID_JOB_DIVISION')
    job_n_job_division1 = relationship(u'JobNJobDivision', primaryjoin='JobNJobPosition.ID_JOB_DIVISION == JobNJobDivision.ID_JOB_DIVISION')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')


class JobNJobPositionLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_position_lang'

    ID_JOB_POSITION_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_POSITION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNJobSpecialSkill(DeclarativeBase2):
    __tablename__ = 'job_n_job_special_skill'

    ID_JOB_SPECIAL_SKILL = Column(BigInteger, primary_key=True)
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision')


class JobNJobSpecialSkillLang(DeclarativeBase2):
    __tablename__ = 'job_n_job_special_skill_lang'

    ID_JOB_SPECIAL_SKILL_LANG = Column(BigInteger, primary_key=True)
    ID_JOB_SPECIAL_SKILL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNKnowWeb(DeclarativeBase2):
    __tablename__ = 'job_n_know_web'

    ID_KNOW_WEB = Column(BigInteger, primary_key=True)
    ID_KNOW_WEB_TYPE = Column(ForeignKey(u'job_n_know_web_type.ID_KNOW_WEB_TYPE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_know_web_type = relationship(u'JobNKnowWebType')


class JobNKnowWebLang(DeclarativeBase2):
    __tablename__ = 'job_n_know_web_lang'

    ID_KNOW_WEB_LANG = Column(BigInteger, primary_key=True)
    ID_KNOW_WEB = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNKnowWebType(DeclarativeBase2):
    __tablename__ = 'job_n_know_web_type'

    ID_KNOW_WEB_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNKnowWebTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_know_web_type_lang'

    ID_KNOW_WEB_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_KNOW_WEB_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLanguage(DeclarativeBase2):
    __tablename__ = 'job_n_language'

    ID_LANGUAGE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    NAME_LOCAL = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLanguageLang(DeclarativeBase2):
    __tablename__ = 'job_n_language_lang'

    ID_LANGUAGE_LANG = Column(BigInteger, primary_key=True)
    ID_LANGUAGE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLanguageStandardizedTest(DeclarativeBase2):
    __tablename__ = 'job_n_language_standardized_test'

    ID_LANGUAGE_STANDARDIZED_TEST = Column(BigInteger, primary_key=True)
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_language = relationship(u'JobNLanguage')


class JobNLanguageStandardizedTestLang(DeclarativeBase2):
    __tablename__ = 'job_n_language_standardized_test_lang'

    ID_LANGUAGE_STANDARDIZED_TEST_LANG = Column(BigInteger, primary_key=True)
    ID_LANGUAGE_STANDARDIZED_TEST = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLanguageStandardizedTestLevel(DeclarativeBase2):
    __tablename__ = 'job_n_language_standardized_test_level'

    ID_LANGUAGE_STANDARDIZED_TEST_LEVEL = Column(BigInteger, primary_key=True)
    ID_LANGUAGE_STANDARDIZED_TEST = Column(ForeignKey(u'job_n_language_standardized_test.ID_LANGUAGE_STANDARDIZED_TEST'), nullable=False, index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_language_standardized_test = relationship(u'JobNLanguageStandardizedTest')


class JobNLanguageStandardizedTestLevelLang(DeclarativeBase2):
    __tablename__ = 'job_n_language_standardized_test_level_lang'

    ID_LANGUAGE_STANDARDIZED_TEST_LEVEL_LANG = Column(BigInteger, primary_key=True)
    ID_LANGUAGE_STANDARDIZED_TEST_LEVEL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLeavingDismissed(DeclarativeBase2):
    __tablename__ = 'job_n_leaving_dismissed'

    ID_LEAVING_DISMISSED = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLeavingDismissedLang(DeclarativeBase2):
    __tablename__ = 'job_n_leaving_dismissed_lang'

    ID_LEAVING_DISMISSED_LANG = Column(BigInteger, primary_key=True)
    ID_LEAVING_DISMISSED = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLeavingResignation(DeclarativeBase2):
    __tablename__ = 'job_n_leaving_resignation'

    ID_LEAVING_RESIGNATION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLeavingResignationLang(DeclarativeBase2):
    __tablename__ = 'job_n_leaving_resignation_lang'

    ID_LEAVING_RESIGNATION_LANG = Column(BigInteger, primary_key=True)
    ID_LEAVING_RESIGNATION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLivingCondition(DeclarativeBase2):
    __tablename__ = 'job_n_living_condition'

    ID_LIVING_CONDITION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNLivingConditionLang(DeclarativeBase2):
    __tablename__ = 'job_n_living_condition_lang'

    ID_LIVING_CONDITION_LANG = Column(BigInteger, primary_key=True)
    ID_LIVING_CONDITION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMajor(DeclarativeBase2):
    __tablename__ = 'job_n_major'

    ID_MAJOR = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMajorLang(DeclarativeBase2):
    __tablename__ = 'job_n_major_lang'

    ID_MAJOR_LANG = Column(BigInteger, primary_key=True)
    ID_MAJOR = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMaritalStatu(DeclarativeBase2):
    __tablename__ = 'job_n_marital_status'

    ID_MARITAL_STATUS = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    CHOICE_MARITAL_TYPE = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMaritalStatusLang(DeclarativeBase2):
    __tablename__ = 'job_n_marital_status_lang'

    ID_MARITAL_STATUS_LANG = Column(BigInteger, primary_key=True)
    ID_MARITAL_STATUS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMilitaryExempted(DeclarativeBase2):
    __tablename__ = 'job_n_military_exempted'

    ID_MILITARY_EXEMPTED = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMilitaryExemptedLang(DeclarativeBase2):
    __tablename__ = 'job_n_military_exempted_lang'

    ID_MILITARY_EXEMPTED_LANG = Column(BigInteger, primary_key=True)
    ID_MILITARY_EXEMPTED = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMilitaryStatu(DeclarativeBase2):
    __tablename__ = 'job_n_military_status'

    ID_MILITARY_STATUS = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    IS_VACANCY = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMilitaryStatusLang(DeclarativeBase2):
    __tablename__ = 'job_n_military_status_lang'

    ID_MILITARY_STATUS_LANG = Column(BigInteger, primary_key=True)
    ID_MILITARY_STATUS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNMultiMapExperience(DeclarativeBase2):
    __tablename__ = 'job_n_multi_map_experience'
    __table_args__ = (
        Index('ID_MULTI_MAP', 'ID_JOB_INDUSTRY', 'ID_JOB_DIVISION', 'ID_JOB_HIERARCHY', 'ID_JOB_EXPERIENCE', unique=True),
    )

    ID_MULTI_MAP_EXPERIENCE = Column(BigInteger, primary_key=True)
    ID_JOB_INDUSTRY = Column(ForeignKey(u'job_n_job_industry.ID_JOB_INDUSTRY'))
    ID_JOB_DIVISION = Column(ForeignKey(u'job_n_job_division.ID_JOB_DIVISION'), index=True)
    ID_JOB_HIERARCHY = Column(ForeignKey(u'job_n_job_hierarchy.ID_JOB_HIERARCHY'), index=True)
    ID_JOB_EXPERIENCE = Column(ForeignKey(u'job_n_job_experience.ID_JOB_EXPERIENCE'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_job_division = relationship(u'JobNJobDivision')
    job_n_job_experience = relationship(u'JobNJobExperience')
    job_n_job_hierarchy = relationship(u'JobNJobHierarchy')
    job_n_job_industry = relationship(u'JobNJobIndustry')


class JobNNationality(DeclarativeBase2):
    __tablename__ = 'job_n_nationality'

    ID_NATIONALITY = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNNationalityLang(DeclarativeBase2):
    __tablename__ = 'job_n_nationality_lang'

    ID_NATIONALITY_LANG = Column(BigInteger, primary_key=True)
    ID_NATIONALITY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNNoOfEmployee(DeclarativeBase2):
    __tablename__ = 'job_n_no_of_employee'

    ID_NO_OF_EMPLOYEE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNNoOfEmployeeLang(DeclarativeBase2):
    __tablename__ = 'job_n_no_of_employee_lang'

    ID_NO_OF_EMPLOYEE_LANG = Column(BigInteger, primary_key=True)
    ID_NO_OF_EMPLOYEE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNOfficeMachineSkill(DeclarativeBase2):
    __tablename__ = 'job_n_office_machine_skill'

    ID_OFFICE_MACHINE_SKILL = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNOfficeMachineSkillLang(DeclarativeBase2):
    __tablename__ = 'job_n_office_machine_skill_lang'

    ID_OFFICE_MACHINE_SKILL_LANG = Column(BigInteger, primary_key=True)
    ID_OFFICE_MACHINE_SKILL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPaidUpCapital(DeclarativeBase2):
    __tablename__ = 'job_n_paid_up_capital'

    ID_PAID_UP_CAPITAL = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    MIN = Column(Numeric(20, 2))
    MAX = Column(Numeric(20, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPaidUpCapitalLang(DeclarativeBase2):
    __tablename__ = 'job_n_paid_up_capital_lang'

    ID_PAID_UP_CAPITAL_LANG = Column(BigInteger, primary_key=True)
    ID_PAID_UP_CAPITAL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPassportType(DeclarativeBase2):
    __tablename__ = 'job_n_passport_type'

    ID_PASSPORT_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPassportTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_passport_type_lang'

    ID_PASSPORT_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_PASSPORT_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPerAmountLang(DeclarativeBase2):
    __tablename__ = 'job_n_per_amount_lang'

    ID_PER_AMOUNT_LANG = Column(BigInteger, primary_key=True)
    ID_PER_AMOUNT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPercentMatch(DeclarativeBase2):
    __tablename__ = 'job_n_percent_match'

    ID_PERCENT_MATCH = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPercentMatchLang(DeclarativeBase2):
    __tablename__ = 'job_n_percent_match_lang'

    ID_PERCENT_MATCH_LANG = Column(BigInteger, primary_key=True)
    ID_PERCENT_MATCH = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPersonalPastRecord(DeclarativeBase2):
    __tablename__ = 'job_n_personal_past_record'

    ID_PERSONAL_PAST_RECORD = Column(BigInteger, primary_key=True)
    ID_PERSONAL_PAST_RECORD_GROUP = Column(ForeignKey(u'job_n_personal_past_record_group.ID_PERSONAL_PAST_RECORD_GROUP'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    SEQ_FOR_APPLICANT = Column(SmallInteger)
    QUESTION_FOR_APPLICANT = Column(Text)
    SEQ_FOR_CORPORATE = Column(SmallInteger)
    QUESTION_FOR_CORPORATE = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_personal_past_record_group = relationship(u'JobNPersonalPastRecordGroup')


class JobNPersonalPastRecordAnswer(DeclarativeBase2):
    __tablename__ = 'job_n_personal_past_record_answer'

    ID_PERSONAL_PAST_RECORD_ANSWER = Column(BigInteger, primary_key=True)
    ID_PERSONAL_PAST_RECORD = Column(ForeignKey(u'job_n_personal_past_record.ID_PERSONAL_PAST_RECORD'), nullable=False, index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    SEQ_FOR_APPLICANT = Column(SmallInteger)
    ANSWER_FOR_APPLICANT = Column(Text)
    SEQ_FOR_CORPORATE = Column(SmallInteger)
    ANSWER_FOR_CORPORATE = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_personal_past_record = relationship(u'JobNPersonalPastRecord')


class JobNPersonalPastRecordAnswerLang(DeclarativeBase2):
    __tablename__ = 'job_n_personal_past_record_answer_lang'

    ID_PERSONAL_PAST_RECORD_ANSWER_LANG = Column(BigInteger, primary_key=True)
    ID_PERSONAL_PAST_RECORD_ANSWER = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    ANSWER_FOR_APPLICANT = Column(Text)
    ANSWER_FOR_CORPORATE = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPersonalPastRecordGroup(DeclarativeBase2):
    __tablename__ = 'job_n_personal_past_record_group'

    ID_PERSONAL_PAST_RECORD_GROUP = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPersonalPastRecordGroupLang(DeclarativeBase2):
    __tablename__ = 'job_n_personal_past_record_group_lang'

    ID_PERSONAL_PAST_RECORD_GROUP_LANG = Column(BigInteger, primary_key=True)
    ID_PERSONAL_PAST_RECORD_GROUP = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPersonalPastRecordLang(DeclarativeBase2):
    __tablename__ = 'job_n_personal_past_record_lang'

    ID_PERSONAL_PAST_RECORD_LANG = Column(BigInteger, primary_key=True)
    ID_PERSONAL_PAST_RECORD = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    QUESTION_FOR_APPLICANT = Column(Text)
    QUESTION_FOR_CORPORATE = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPersonalSkill(DeclarativeBase2):
    __tablename__ = 'job_n_personal_skill'

    ID_PERSONAL_SKILL = Column(BigInteger, primary_key=True)
    ID_PERSONAL_SKILL_GROUP = Column(ForeignKey(u'job_n_personal_skill_group.ID_PERSONAL_SKILL_GROUP'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_personal_skill_group = relationship(u'JobNPersonalSkillGroup')


class JobNPersonalSkillGroup(DeclarativeBase2):
    __tablename__ = 'job_n_personal_skill_group'

    ID_PERSONAL_SKILL_GROUP = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPersonalSkillGroupLang(DeclarativeBase2):
    __tablename__ = 'job_n_personal_skill_group_lang'

    ID_PERSONAL_SKILL_GROUP_LANG = Column(BigInteger, primary_key=True)
    ID_PERSONAL_SKILL_GROUP = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPersonalSkillLang(DeclarativeBase2):
    __tablename__ = 'job_n_personal_skill_lang'

    ID_PERSONAL_SKILL_LANG = Column(BigInteger, primary_key=True)
    ID_PERSONAL_SKILL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPhoneType(DeclarativeBase2):
    __tablename__ = 'job_n_phone_type'

    ID_PHONE_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPhoneTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_phone_type_lang'

    ID_PHONE_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_PHONE_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPrefixName(DeclarativeBase2):
    __tablename__ = 'job_n_prefix_name'

    ID_PREFIX_NAME = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255), nullable=False)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPrefixNameLang(DeclarativeBase2):
    __tablename__ = 'job_n_prefix_name_lang'

    ID_PREFIX_NAME_LANG = Column(BigInteger, primary_key=True)
    ID_PREFIX_NAME = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProfessionalLicense(DeclarativeBase2):
    __tablename__ = 'job_n_professional_license'

    ID_PROFESSIONAL_LICENSE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProfessionalLicenseLang(DeclarativeBase2):
    __tablename__ = 'job_n_professional_license_lang'

    ID_PROFESSIONAL_LICENSE_LANG = Column(BigInteger, primary_key=True)
    ID_PROFESSIONAL_LICENSE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProficiencyLanguage(DeclarativeBase2):
    __tablename__ = 'job_n_proficiency_language'

    ID_PROFICIENCY_LANGUAGE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProficiencyLanguageLang(DeclarativeBase2):
    __tablename__ = 'job_n_proficiency_language_lang'

    ID_PROFICIENCY_LANGUAGE_LANG = Column(BigInteger, primary_key=True)
    ID_PROFICIENCY_LANGUAGE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProficiencySkillComputer(DeclarativeBase2):
    __tablename__ = 'job_n_proficiency_skill_computer'

    ID_PROFICIENCY_SKILL_COMPUTER = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProficiencySkillComputerLang(DeclarativeBase2):
    __tablename__ = 'job_n_proficiency_skill_computer_lang'

    ID_PROFICIENCY_SKILL_COMPUTER_LANG = Column(BigInteger, primary_key=True)
    ID_PROFICIENCY_SKILL_COMPUTER = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProfitPerYear(DeclarativeBase2):
    __tablename__ = 'job_n_profit_per_year'

    ID_PROFIT_PER_YEAR = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    MIN = Column(Numeric(20, 2))
    MAX = Column(Numeric(20, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProfitPerYearLang(DeclarativeBase2):
    __tablename__ = 'job_n_profit_per_year_lang'

    ID_PROFIT_PER_YEAR_LANG = Column(BigInteger, primary_key=True)
    ID_PROFIT_PER_YEAR = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNProvince(DeclarativeBase2):
    __tablename__ = 'job_n_province'

    ID_PROVINCE = Column(BigInteger, primary_key=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_ZONE = Column(ForeignKey(u'job_n_zone.ID_ZONE'), index=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_country = relationship(u'JobNCountry')
    job_n_zone = relationship(u'JobNZone')


class JobNProvinceLang(DeclarativeBase2):
    __tablename__ = 'job_n_province_lang'

    ID_PROVINCE_LANG = Column(BigInteger, primary_key=True)
    ID_PROVINCE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNPublicTransportation(DeclarativeBase2):
    __tablename__ = 'job_n_public_transportation'

    ID_PUBLIC_TRANSPORTATION = Column(BigInteger, primary_key=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_province = relationship(u'JobNProvince')


class JobNPublicTransportationLang(DeclarativeBase2):
    __tablename__ = 'job_n_public_transportation_lang'

    ID_PUBLIC_TRANSPORTATION_LANG = Column(BigInteger, primary_key=True)
    ID_PUBLIC_TRANSPORTATION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRace(DeclarativeBase2):
    __tablename__ = 'job_n_race'

    ID_RACE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRaceLang(DeclarativeBase2):
    __tablename__ = 'job_n_race_lang'

    ID_RACE_LANG = Column(BigInteger, primary_key=True)
    ID_RACE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNReadyWork(DeclarativeBase2):
    __tablename__ = 'job_n_ready_work'

    ID_READY_WORK = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNReadyWorkLang(DeclarativeBase2):
    __tablename__ = 'job_n_ready_work_lang'

    ID_READY_WORK_LANG = Column(BigInteger, primary_key=True)
    ID_READY_WORK = Column(ForeignKey(u'job_n_ready_work.ID_READY_WORK'), index=True)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))

    job_n_ready_work = relationship(u'JobNReadyWork')


class JobNRecommendIntroduce(DeclarativeBase2):
    __tablename__ = 'job_n_recommend_introduce'

    ID_RECOMMEND_INTRODUCE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRecommendIntroduceLang(DeclarativeBase2):
    __tablename__ = 'job_n_recommend_introduce_lang'

    ID_RECOMMEND_INTRODUCE_LANG = Column(BigInteger, primary_key=True)
    ID_RECOMMEND_INTRODUCE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRegion(DeclarativeBase2):
    __tablename__ = 'job_n_region'

    ID_REGION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRegionLang(DeclarativeBase2):
    __tablename__ = 'job_n_region_lang'

    ID_REGION_LANG = Column(BigInteger, primary_key=True)
    ID_REGION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRegisterCapital(DeclarativeBase2):
    __tablename__ = 'job_n_register_capital'

    ID_REGISTER_CAPITAL = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    MIN = Column(Numeric(20, 2))
    MAX = Column(Numeric(20, 2))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRegisterCapitalLang(DeclarativeBase2):
    __tablename__ = 'job_n_register_capital_lang'

    ID_REGISTER_CAPITAL_LANG = Column(BigInteger, primary_key=True)
    ID_REGISTER_CAPITAL = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRelationship(DeclarativeBase2):
    __tablename__ = 'job_n_relationship'

    ID_RELATIONSHIP = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRelationshipLang(DeclarativeBase2):
    __tablename__ = 'job_n_relationship_lang'

    ID_RELATIONSHIP_LANG = Column(BigInteger, primary_key=True)
    ID_RELATIONSHIP = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNReligion(DeclarativeBase2):
    __tablename__ = 'job_n_religion'

    ID_RELIGION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNReligionLang(DeclarativeBase2):
    __tablename__ = 'job_n_religion_lang'

    ID_RELIGION_LANG = Column(BigInteger, primary_key=True)
    ID_RELIGION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRepeatTime(DeclarativeBase2):
    __tablename__ = 'job_n_repeat_time'

    ID_REPEAT_TIME = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNRepeatTimeLang(DeclarativeBase2):
    __tablename__ = 'job_n_repeat_time_lang'

    ID_REPEAT_TIME_LANG = Column(BigInteger, primary_key=True)
    ID_REPEAT_TIME = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSalaryBase(DeclarativeBase2):
    __tablename__ = 'job_n_salary_base'

    ID_SALARY_BASE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSalaryBaseLang(DeclarativeBase2):
    __tablename__ = 'job_n_salary_base_lang'

    ID_SALARY_BASE_LANG = Column(BigInteger, primary_key=True)
    ID_SALARY_BASE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSalaryPerAmount(DeclarativeBase2):
    __tablename__ = 'job_n_salary_per_amount'

    ID_SALARY_PER_AMOUNT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSalaryPerAmountLang(DeclarativeBase2):
    __tablename__ = 'job_n_salary_per_amount_lang'

    ID_SALARY_PER_AMOUNT_LANG = Column(BigInteger, primary_key=True)
    ID_SALARY_PER_AMOUNT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSocialNetwork(DeclarativeBase2):
    __tablename__ = 'job_n_social_network'

    ID_SOCIAL_NETWORK = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    IMAGE_LOGO_PATH = Column(String(255))
    TIP = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSocialNetworkLang(DeclarativeBase2):
    __tablename__ = 'job_n_social_network_lang'

    ID_SOCIAL_NETWORK_LANG = Column(BigInteger, primary_key=True)
    ID_SOCIAL_NETWORK = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    TIP = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSpecialSkillComputer(DeclarativeBase2):
    __tablename__ = 'job_n_special_skill_computer'

    ID_SPECIAL_SKILL_COMPUTER = Column(BigInteger, primary_key=True)
    ID_SPECIAL_SKILL_COMPUTER_TYPE = Column(ForeignKey(u'job_n_special_skill_computer_type.ID_SPECIAL_SKILL_COMPUTER_TYPE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_special_skill_computer_type = relationship(u'JobNSpecialSkillComputerType')


class JobNSpecialSkillComputerLang(DeclarativeBase2):
    __tablename__ = 'job_n_special_skill_computer_lang'

    ID_SPECIAL_SKILL_COMPUTER_LANG = Column(BigInteger, primary_key=True)
    ID_SPECIAL_SKILL_COMPUTER = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSpecialSkillComputerType(DeclarativeBase2):
    __tablename__ = 'job_n_special_skill_computer_type'

    ID_SPECIAL_SKILL_COMPUTER_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSpecialSkillComputerTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_special_skill_computer_type_lang'

    ID_SPECIAL_SKILL_COMPUTER_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_SPECIAL_SKILL_COMPUTER_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNStation(DeclarativeBase2):
    __tablename__ = 'job_n_station'

    ID_STATION = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNStationLang(DeclarativeBase2):
    __tablename__ = 'job_n_station_lang'

    ID_STATION_LANG = Column(BigInteger, primary_key=True)
    ID_STATION = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNSuperResumeFormat(DeclarativeBase2):
    __tablename__ = 'job_n_super_resume_format'

    ID_SUPER_RESUME_FORMAT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    PATH_FILE = Column(String(400))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    UPDATE_USER = Column(String(255))


class JobNTest(DeclarativeBase2):
    __tablename__ = 'job_n_test'

    ID_TEST = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNTestLang(DeclarativeBase2):
    __tablename__ = 'job_n_test_lang'

    ID_TEST_LANG = Column(BigInteger, primary_key=True)
    ID_TEST = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNTimeZone(DeclarativeBase2):
    __tablename__ = 'job_n_time_zone'

    ID_TIME_ZONE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNTimeZoneLang(DeclarativeBase2):
    __tablename__ = 'job_n_time_zone_lang'

    ID_TIME_ZONE_LANG = Column(BigInteger, primary_key=True)
    ID_TIME_ZONE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNUnit(DeclarativeBase2):
    __tablename__ = 'job_n_unit'

    ID_UNIT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNUnitLang(DeclarativeBase2):
    __tablename__ = 'job_n_unit_lang'

    ID_UNIT_LANG = Column(BigInteger, primary_key=True)
    ID_UNIT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNUnitLength(DeclarativeBase2):
    __tablename__ = 'job_n_unit_length'

    ID_UNIT_LENGTH = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNUnitLengthLang(DeclarativeBase2):
    __tablename__ = 'job_n_unit_length_lang'

    ID_UNIT_LENGTH_LANG = Column(BigInteger, primary_key=True)
    ID_UNIT_LENGTH = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNUniversity(DeclarativeBase2):
    __tablename__ = 'job_n_university'

    ID_UNIVERSITY = Column(BigInteger, primary_key=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), nullable=False, index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    ID_COUNTY = Column(ForeignKey(u'job_n_county.ID_COUNTY'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_county = relationship(u'JobNCounty')
    job_n_province = relationship(u'JobNProvince')


class JobNUniversityLang(DeclarativeBase2):
    __tablename__ = 'job_n_university_lang'

    ID_UNIVERSITY_LANG = Column(BigInteger, primary_key=True)
    ID_UNIVERSITY = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNVehicle(DeclarativeBase2):
    __tablename__ = 'job_n_vehicle'

    ID_VEHICLE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNVehicleClas(DeclarativeBase2):
    __tablename__ = 'job_n_vehicle_class'

    ID_VEHICLE_CLASS = Column(BigInteger, primary_key=True)
    ID_VEHICLE = Column(ForeignKey(u'job_n_vehicle.ID_VEHICLE'), index=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_vehicle = relationship(u'JobNVehicle')


class JobNVehicleClassLang(DeclarativeBase2):
    __tablename__ = 'job_n_vehicle_class_lang'

    ID_VEHICLE_CLASS_LANG = Column(BigInteger, primary_key=True)
    ID_VEHICLE_CLASS = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNVehicleLang(DeclarativeBase2):
    __tablename__ = 'job_n_vehicle_lang'

    ID_VEHICLE_LANG = Column(BigInteger, primary_key=True)
    ID_VEHICLE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNVisaType(DeclarativeBase2):
    __tablename__ = 'job_n_visa_type'

    ID_VISA_TYPE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNVisaTypeLang(DeclarativeBase2):
    __tablename__ = 'job_n_visa_type_lang'

    ID_VISA_TYPE_LANG = Column(BigInteger, primary_key=True)
    ID_VISA_TYPE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNWebBoConfig(DeclarativeBase2):
    __tablename__ = 'job_n_web_bo_config'

    ID_WEB_BO_CONFIG = Column(BigInteger, primary_key=True)
    ID_WEB_BO_CONFIG_GEOGRAPHY = Column(BigInteger, index=True)
    ID_WEB_BO_CONFIG_PAGE_MODULE = Column(BigInteger, index=True)
    IS_DISPLAY = Column(String(1))
    IS_MANDATORY = Column(String(1))
    IS_MATCH = Column(String(1))
    IS_WEIGHT = Column(String(1))
    WEIGHT_PERCENT = Column(Numeric(5, 2))
    DESCRIPTION = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNWebBoConfigGeography(DeclarativeBase2):
    __tablename__ = 'job_n_web_bo_config_geography'

    ID_WEB_BO_CONFIG_GEOGRAPHY = Column(BigInteger, primary_key=True)
    ID_REGION = Column(ForeignKey(u'job_n_region.ID_REGION'), index=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_ZONE = Column(ForeignKey(u'job_n_zone.ID_ZONE'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CITY = Column(ForeignKey(u'job_n_city.ID_CITY'), index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_city = relationship(u'JobNCity')
    job_n_country = relationship(u'JobNCountry')
    job_n_province = relationship(u'JobNProvince')
    job_n_region = relationship(u'JobNRegion')
    job_n_zone = relationship(u'JobNZone')


class JobNWebBoConfigPageModule(DeclarativeBase2):
    __tablename__ = 'job_n_web_bo_config_page_module'

    ID_WEB_BO_CONFIG_PAGE_MODULE = Column(BigInteger, primary_key=True)
    PAGE = Column(String(255))
    MODULE = Column(String(255))
    FIELD = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNWebBoConfigPageModuleLang(DeclarativeBase2):
    __tablename__ = 'job_n_web_bo_config_page_module_lang'

    ID_WEB_BO_CONFIG_PAGE_MODULE_LANG = Column(BigInteger, primary_key=True)
    ID_WEB_BO_CONFIG_PAGE_MODULE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    PAGE = Column(String(255))
    MODULE = Column(String(255))
    FIELD = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNWeightUnit(DeclarativeBase2):
    __tablename__ = 'job_n_weight_unit'

    ID_WEIGHT_UNIT = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNWeightUnitLang(DeclarativeBase2):
    __tablename__ = 'job_n_weight_unit_lang'

    ID_WEIGHT_UNIT_LANG = Column(BigInteger, primary_key=True)
    ID_WEIGHT_UNIT = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNZipcode(DeclarativeBase2):
    __tablename__ = 'job_n_zipcode'

    ID_ZIPCODE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNZipcodeLang(DeclarativeBase2):
    __tablename__ = 'job_n_zipcode_lang'

    ID_ZIPCODE_LANG = Column(BigInteger, primary_key=True)
    ID_ZIPCODE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNZone(DeclarativeBase2):
    __tablename__ = 'job_n_zone'

    ID_ZONE = Column(BigInteger, primary_key=True)
    SEQ = Column(SmallInteger)
    CODE2 = Column(String(2))
    CODE3 = Column(String(3))
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobNZoneLang(DeclarativeBase2):
    __tablename__ = 'job_n_zone_lang'

    ID_ZONE_LANG = Column(BigInteger, primary_key=True)
    ID_ZONE = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class MalMEmail(DeclarativeBase2):
    __tablename__ = 'mal_m_email'

    ID_EMAIL = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    ID_EMAIL_TEMPLATE = Column(BigInteger, nullable=False, index=True)
    EMAIL_NAME = Column(String(128))
    TOTAL_SEND = Column(BigInteger, server_default=text("'0'"))
    TOTAL_SENDED = Column(BigInteger, server_default=text("'0'"))
    TOTAL_SUCCESS = Column(BigInteger, server_default=text("'0'"))
    TOTAL_ERROR = Column(BigInteger, server_default=text("'0'"))
    TOTAL_READED = Column(BigInteger, server_default=text("'0'"))
    TOTAL_OPEN = Column(BigInteger, server_default=text("'0'"))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class MalMEmailLink(DeclarativeBase2):
    __tablename__ = 'mal_m_email_link'

    ID_EMAIL_LINK = Column(BigInteger, primary_key=True)
    ID_EMAIL_TEMPLATE = Column(BigInteger, index=True)
    URL = Column(String(255))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class MalMEmailTemplate(DeclarativeBase2):
    __tablename__ = 'mal_m_email_template'

    ID_EMAIL_TEMPLATE = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger, index=True)
    SUBJECT = Column(String(255))
    PATH = Column(String(255))
    PARAMETER = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class MalTImportEmail(DeclarativeBase2):
    __tablename__ = 'mal_t_import_email'

    ID_IMPORT_EMAIL = Column(BigInteger, primary_key=True, index=True)
    TOTAL_ROWS = Column(Integer)
    SUCCESS_ROWS = Column(Integer)
    DUPLICATE_ROWS = Column(Integer)
    CHOICE_IMPORT_TYPE = Column(String(1))
    IMPORT_DATE = Column(Date)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    UPDATE_DATE = Column(DateTime)


class MalTImportEmailList(DeclarativeBase2):
    __tablename__ = 'mal_t_import_email_list'

    ID_IMPORT_EMAIL_LIST = Column(BigInteger, primary_key=True, index=True)
    ID_IMPORT_EMAIL = Column(ForeignKey(u'mal_t_import_email.ID_IMPORT_EMAIL'), index=True)
    EMAIL = Column(String(255))
    NAME = Column(String(255))
    CHOICE_IMPORT_TYPE = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    UPDATE_DATE = Column(DateTime)

    mal_t_import_email = relationship(u'MalTImportEmail')


class MalTSendEmail(DeclarativeBase2):
    __tablename__ = 'mal_t_send_email'

    ID_SEND_EMAIL = Column(BigInteger, primary_key=True)
    EMAIL_ID = Column(BigInteger, nullable=False)
    EMAIL_TEMPLATE_ID = Column(BigInteger, nullable=False)
    RECEIVE = Column(String(255), nullable=False)
    SUBJECT = Column(String(255))
    PARAMETER = Column(String(255))
    SEND = Column(String(1), server_default=text("'0'"))
    SEND_TIME = Column(DateTime)
    SENDED = Column(String(1), server_default=text("'0'"))
    SENDED_TIME = Column(DateTime)
    READED = Column(Integer, server_default=text("'0'"))
    FIRST_READ_TIME = Column(DateTime)
    LAST_READ_TIME = Column(DateTime)
    ERROR_DESC = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class MalTSendEmailLinkCount(DeclarativeBase2):
    __tablename__ = 'mal_t_send_email_link_count'

    ID_SEND_EMAIL_LINK_COUNT = Column(BigInteger, primary_key=True)
    ID_SEND_EMAIL = Column(BigInteger, index=True)
    EMAIL_LINK_ID = Column(BigInteger)
    CLICK = Column(BigInteger, server_default=text("'0'"))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class MalTSendEmailLinkTime(DeclarativeBase2):
    __tablename__ = 'mal_t_send_email_link_time'

    ID_SEND_EMAIL_LINK_TIME = Column(BigInteger, primary_key=True)
    ID_SEND_EMAIL = Column(BigInteger, index=True)
    EMAIL_LINK_ID = Column(BigInteger)
    CLICK_TIME = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    STATUS = Column(String(1))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SegMCriterion(DeclarativeBase2):
    __tablename__ = 'seg_m_criteria'

    ID_CRITERIA = Column(BigInteger, primary_key=True)
    ID_SEGMENT = Column(ForeignKey(u'seg_m_segment.ID_SEGMENT'), nullable=False, index=True)
    NAME = Column(String(255))
    CRITERIA_TYPE = Column(String(255), nullable=False)
    ID_PARENT = Column(BigInteger)
    LEVEL = Column(Integer)
    SOURCE_TABLE = Column(String(255))
    SOURCE_COLUMN = Column(String(255))
    SOURCE_SQL = Column(Text)
    DESTINATION_TABLE = Column(String(255))
    DESTINATION_COLUMN = Column(String(255))
    DESTINATION_SQL = Column(Text)
    PARAMETER = Column(String(255))
    CONDITION = Column(String(1))
    SQL_BEGIN = Column(Text)
    SQL_SELECT = Column(Text)
    SQL_INSERT = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    seg_m_segment = relationship(u'SegMSegment')


class SegMCriteriaJoin(DeclarativeBase2):
    __tablename__ = 'seg_m_criteria_join'

    ID_CRITERIA_JOIN = Column(BigInteger, primary_key=True)
    ID_CRITERIA = Column(ForeignKey(u'seg_m_criteria.ID_CRITERIA'), index=True)
    TABLE_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    seg_m_criterion = relationship(u'SegMCriterion')


class SegMCriteriaJoinOn(DeclarativeBase2):
    __tablename__ = 'seg_m_criteria_join_on'

    ID_CRITERIA_JOIN_ON = Column(BigInteger, primary_key=True)
    ID_CRITERIA_JOIN = Column(ForeignKey(u'seg_m_criteria_join.ID_CRITERIA_JOIN'), index=True)
    TABLE = Column(String(255))
    COLUMN = Column(String(255))
    OPERATION = Column(String(255))
    TABLE_MAP = Column(String(255))
    COLUMN_MAP = Column(String(255))
    PARAMETER = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    seg_m_criteria_join = relationship(u'SegMCriteriaJoin')


class SegMCriteriaWeight(DeclarativeBase2):
    __tablename__ = 'seg_m_criteria_weight'

    ID_CRITERIA = Column(ForeignKey(u'seg_m_criteria.ID_CRITERIA'), primary_key=True, nullable=False)
    ID_SEGMENT = Column(BigInteger, primary_key=True, nullable=False, index=True)
    KEY = Column(String(255), primary_key=True, nullable=False)
    DATA = Column(String(255), primary_key=True, nullable=False)
    MACTH = Column(String(1))
    WEIGHT = Column(Integer)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    seg_m_criterion = relationship(u'SegMCriterion')


class SegMSegment(DeclarativeBase2):
    __tablename__ = 'seg_m_segment'

    ID_SEGMENT = Column(BigInteger, primary_key=True)
    NAME = Column(String(255))
    KEY_TABLE = Column(String(255))
    KEY_COLUMN = Column(String(255))
    OUT_TABLE = Column(String(255))
    OUT_COLUMN = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SegTSegmentProces(DeclarativeBase2):
    __tablename__ = 'seg_t_segment_process'

    ID_SEGMENT_PROCESS = Column(BigInteger, primary_key=True)
    ID_SEGMENT = Column(ForeignKey(u'seg_m_segment.ID_SEGMENT'), index=True)
    KEY_ID = Column(String(255))
    SQL_RESULT = Column(Text)
    SQL_PARA = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    seg_m_segment = relationship(u'SegMSegment')


class SegTSegmentResult(DeclarativeBase2):
    __tablename__ = 'seg_t_segment_result'
    __table_args__ = (
        Index('ID_SEGMENT', 'ID_SEGMENT', 'KEY_ID', 'OUT_ID', 'ID_SEGMENT_RESULT', unique=True),
    )

    ID_SEGMENT_RESULT = Column(BigInteger, primary_key=True)
    ID_SEGMENT = Column(ForeignKey(u'seg_m_segment.ID_SEGMENT'))
    KEY_ID = Column(String(255))
    OUT_ID = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    seg_m_segment = relationship(u'SegMSegment')


class SysMAction(DeclarativeBase2):
    __tablename__ = 'sys_m_action'

    ID_ACTION = Column(BigInteger, primary_key=True)
    PAGE_NAME = Column(String(50), nullable=False)
    ACTION_NAME = Column(String(50))
    NAME_SPACE = Column(String(50))
    URL = Column(String(255))
    TYPE = Column(String(1), nullable=False)
    ID_MENU = Column(BigInteger)
    ID_FUNCTION = Column(String(32), nullable=False)
    INPUT_RESULT_NAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMCm(DeclarativeBase2):
    __tablename__ = 'sys_m_cms'

    LANG_CODE3 = Column(String(3), primary_key=True, nullable=False)
    PAGE_NAME = Column(String(255), primary_key=True, nullable=False)
    CONTENT = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMConfig(DeclarativeBase2):
    __tablename__ = 'sys_m_config'

    CONFIG_KEY = Column(String(100), primary_key=True)
    CONFIG_VALUE = Column(String(255), nullable=False)
    CONFIG_GROUP = Column(String(100), nullable=False)
    DESC = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMConfigByCode(DeclarativeBase2):
    __tablename__ = 'sys_m_config_by_code'

    CONFIG_KEY = Column(String(100), primary_key=True, nullable=False)
    CONFIG_CODE = Column(String(3), primary_key=True, nullable=False)
    CONFIG_VALUE = Column(String(255), nullable=False)
    CONFIG_GROUP = Column(String(100), nullable=False)
    DESC = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMFieldHelp(DeclarativeBase2):
    __tablename__ = 'sys_m_field_help'

    ID_FIELD_HELP = Column(BigInteger, primary_key=True)
    PAGE = Column(String(255))
    FIELD = Column(String(255))
    HELP_MESSAGE = Column(String(255))
    HELP_MESSAGE_PARAMETER = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMFieldValidator(DeclarativeBase2):
    __tablename__ = 'sys_m_field_validator'
    __table_args__ = (
        Index('PAGE', 'PAGE', 'FIELD'),
    )

    ID_FIELD_VALIDATOR = Column(BigInteger, primary_key=True, nullable=False, index=True)
    CODE = Column(String(3), primary_key=True, nullable=False, server_default=text("'---'"))
    PAGE = Column(String(255))
    FIELD = Column(String(255))
    PRE_CON = Column(BigInteger)
    SEQ = Column(Integer)
    TYPE = Column(String(255))
    PARAMETER = Column(String(255))
    MESSAGE_KEY = Column(String(255))
    MESSAGE = Column(String(255))
    MESSAGE_PARAMETER = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMFunction(DeclarativeBase2):
    __tablename__ = 'sys_m_function'

    ID_FUNCTION = Column(String(32), primary_key=True)
    NAME = Column(String(255), nullable=False)
    LEVEL = Column(SmallInteger, nullable=False)
    ID_PARENT = Column(String(32))
    DESC = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMGenKey(DeclarativeBase2):
    __tablename__ = 'sys_m_gen_key'

    ID_GEN_KEY = Column(BigInteger, primary_key=True)
    USER_ID = Column(BigInteger, nullable=False)
    KEY_GEN = Column(String(255), nullable=False)
    KEY_TYPE = Column(String(2), nullable=False)
    TIME_OUT = Column(DateTime)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMLabel(DeclarativeBase2):
    __tablename__ = 'sys_m_label'

    LANGUAGE = Column(String(50), primary_key=True, nullable=False)
    PAGE = Column(String(50), primary_key=True, nullable=False)
    LABEL = Column(String(50), primary_key=True, nullable=False)
    DISPLAY_TEXT = Column(Text, nullable=False)
    DESC = Column(Text)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMMenu(DeclarativeBase2):
    __tablename__ = 'sys_m_menu'

    ID_MENU = Column(BigInteger, primary_key=True)
    NAME = Column(String(50), nullable=False)
    LEVEL = Column(SmallInteger, nullable=False)
    MENU_TYPE = Column(String(1))
    ID_PARENT = Column(BigInteger)
    ID_ACTION = Column(BigInteger)
    SEQ = Column(Integer)
    ID_FUNCTION = Column(String(32), nullable=False)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMMessage(DeclarativeBase2):
    __tablename__ = 'sys_m_message'

    MESSAGE_CODE = Column(String(50), primary_key=True, nullable=False)
    MESSAGE_LANG = Column(String(10), primary_key=True, nullable=False)
    DISPLAY_TEXT = Column(String(255), nullable=False)
    MESSAGE_DESC = Column(String(255))
    MESSAGE_TYPE = Column(String(10), nullable=False)
    SOLUTION = Column(String(255))
    REMARK = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMRole(DeclarativeBase2):
    __tablename__ = 'sys_m_role'

    ID_ROLE = Column(BigInteger, primary_key=True)
    ROLE_NAME = Column(String(64), nullable=False)
    DESC = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMRoleMapFunction(DeclarativeBase2):
    __tablename__ = 'sys_m_role_map_function'

    ID_ROLE = Column(BigInteger, primary_key=True, nullable=False)
    ID_FUNCTION = Column(String(32), primary_key=True, nullable=False)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMUser(DeclarativeBase2):
    __tablename__ = 'sys_m_user'

    ID_USER = Column(BigInteger, primary_key=True)
    USERNAME = Column(String(255), nullable=False)
    PASSWORD = Column(String(32))
    ID_PREFIX_NAME = Column(BigInteger)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMUserInvite(SysMUser):
    __tablename__ = 'job_m_user_invite'

    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), primary_key=True)
    ID_USER_INVITE = Column(BigInteger, index=True)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class JobMUserGeneralSetting(SysMUser):
    __tablename__ = 'job_m_user_general_setting'

    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), primary_key=True, server_default=text("'0'"))
    ID_LANGUAGE = Column(ForeignKey(u'job_n_language.ID_LANGUAGE'), index=True)
    ID_TIME_ZONE = Column(ForeignKey(u'job_n_time_zone.ID_TIME_ZONE'), index=True)
    ID_COUNTRY = Column(ForeignKey(u'job_n_country.ID_COUNTRY'), index=True)
    ID_PROVINCE = Column(ForeignKey(u'job_n_province.ID_PROVINCE'), index=True)
    ID_CURRENCY = Column(ForeignKey(u'job_n_currency.ID_CURRENCY'), index=True)
    MANY_POSITION = Column(Integer)
    IS_USE_SERVICE = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_n_country = relationship(u'JobNCountry')
    job_n_currency = relationship(u'JobNCurrency')
    job_n_language = relationship(u'JobNLanguage')
    job_n_province = relationship(u'JobNProvince')
    job_n_time_zone = relationship(u'JobNTimeZone')


class JobCUserCorporate(SysMUser):
    __tablename__ = 'job_c_user_corporate'

    ID_USER = Column(ForeignKey(u'sys_m_user.ID_USER'), primary_key=True)
    ID_CORPORATE = Column(ForeignKey(u'job_c_corporate.ID_CORPORATE'), index=True)
    IS_ADMIN_CORPORATE = Column(String(1))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))

    job_c_corporate = relationship(u'JobCCorporate')


class SysMUserLang(DeclarativeBase2):
    __tablename__ = 'sys_m_user_lang'

    ID_USER_LANG = Column(BigInteger, primary_key=True)
    ID_USER = Column(BigInteger)
    LANG_CODE3 = Column(String(3), nullable=False)
    FIRST_NAME = Column(String(255))
    MID_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    MAIDEN_SURNAME = Column(String(255))
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))


class SysMUserMapRole(DeclarativeBase2):
    __tablename__ = 'sys_m_user_map_role'

    ID_USER = Column(BigInteger, primary_key=True, nullable=False)
    ID_ROLE = Column(BigInteger, primary_key=True, nullable=False)
    STATUS = Column(String(1), server_default=text("'A'"))
    CREATE_DATE = Column(DateTime)
    CREATE_USER = Column(String(255))
    UPDATE_DATE = Column(DateTime)
    UPDATE_USER = Column(String(255))
