# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Answer(Base):
    __tablename__ = 'answer'
    __table_args__ = {'comment': 'This is are our answers'}

    id = Column(String(50, 'utf8_unicode_ci'), primary_key=True)
    question_option_id = Column(INTEGER(11), index=True)
    answer_text = Column(String(255, 'utf8_unicode_ci'))
    completed_survey_id = Column(String(50, 'utf8_unicode_ci'), nullable=False)
    image_url = Column(String(200, 'utf8_unicode_ci'))
    question_id = Column(INTEGER(11), nullable=False, index=True)


class InputType(Base):
    __tablename__ = 'input_type'
    __table_args__ = {'comment': 'This is our survey tool.'}

    id = Column(INTEGER(11), primary_key=True)
    input_type_name = Column(String(80, 'utf8_unicode_ci'), nullable=False, unique=True)


class OptionChoice(Base):
    __tablename__ = 'option_choice'
    __table_args__ = {'comment': 'This is our survey tool.'}

    id = Column(INTEGER(11), primary_key=True)
    option_choice_name = Column(String(45, 'utf8_unicode_ci'), nullable=False)


class Project(Base):
    __tablename__ = 'project'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(100), nullable=False)


class QuestionImage(Base):
    __tablename__ = 'question_image'

    id = Column(INTEGER(11), primary_key=True)
    url = Column(String(350, 'utf8_unicode_ci'))


class QuestionOption(Base):
    __tablename__ = 'question_option'

    id = Column(INTEGER(11), primary_key=True)
    question_id = Column(INTEGER(11), nullable=False, index=True)
    option_choice_id = Column(INTEGER(11), nullable=False, index=True)


class Stat(Base):
    __tablename__ = 'stat'

    id = Column(INTEGER(11), primary_key=True)
    modification_date = Column(MEDIUMTEXT, server_default=text("0"))


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': 'User table to store the additional infos from firebase user. '}

    id = Column(INTEGER(11), primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    firebase_id = Column(String(100), nullable=False, unique=True)
    email = Column(String(100))
    type = Column(INTEGER(11), nullable=False)


class Village(Base):
    __tablename__ = 'village'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)


class Interviewee(Base):
    __tablename__ = 'interviewee'
    __table_args__ = {'comment': 'This is our survey tool.'}

    id = Column(String(50, 'utf8_unicode_ci'), primary_key=True)
    name = Column(String(45, 'utf8_unicode_ci'))
    village_id = Column(ForeignKey('village.id'), index=True)
    user_id = Column(ForeignKey('user.id'), index=True)
    image_url = Column(String(250, 'utf8_unicode_ci'))

    user = relationship('User')
    village = relationship('Village')


class SurveyHeader(Base):
    __tablename__ = 'survey_header'
    __table_args__ = {'comment': 'This is our survey tool.'}

    id = Column(INTEGER(11), primary_key=True)
    survey_name = Column(String(80, 'utf8_unicode_ci'), unique=True)
    project_id = Column(ForeignKey('project.id'), index=True)

    project = relationship('Project')


class CompletedSurvey(Base):
    __tablename__ = 'completed_survey'

    id = Column(String(50), primary_key=True)
    interviewee_id = Column(String(50), nullable=False)
    survey_header_id = Column(ForeignKey('survey_header.id'), nullable=False, index=True)
    creation_date = Column(String(50))
    user_id = Column(ForeignKey('user.id'), index=True)
    longitude = Column(Float(asdecimal=True))
    latitude = Column(Float(asdecimal=True))

    survey_header = relationship('SurveyHeader')
    user = relationship('User')


class SurveySection(Base):
    __tablename__ = 'survey_section'
    __table_args__ = {'comment': 'This is our survey tool.'}

    id = Column(INTEGER(11), primary_key=True)
    survey_header_id = Column(ForeignKey('survey_header.id'), index=True)
    section_name = Column(String(200, 'utf8_unicode_ci'))

    survey_header = relationship('SurveyHeader')


class Question(Base):
    __tablename__ = 'question'
    __table_args__ = {'comment': 'This is are our questions'}

    id = Column(INTEGER(11), primary_key=True)
    survey_section_id = Column(ForeignKey('survey_section.id'), nullable=False, index=True)
    input_type_id = Column(ForeignKey('input_type.id'), nullable=False, index=True)
    question_name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    dependent_question_id = Column(INTEGER(11))
    dependent_question_option_id = Column(INTEGER(11))
    question_images_id = Column(ForeignKey('question_image.id'), index=True)

    input_type = relationship('InputType')
    question_images = relationship('QuestionImage')
    survey_section = relationship('SurveySection')
