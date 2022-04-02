#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------


from Entities import *


class Studentdetailsextended(Base):
    __tablename__ = 'studentdetailsextended'

    studentExId = Column(Integer, primary_key=True, index=True)
    studentExStudentId = Column(ForeignKey('studentdetails.studentId', ondelete='CASCADE'), index=True)
    studentTenthCGPA = Column(Float)
    studentTwelfthCGPA = Column(Float)
    studentTenthPercentage = Column(Float)
    studentTwelfthPercentage = Column(Float)
    studentFirstSemCGPA = Column(Float)
    studentSecondSemCGPA = Column(Float)
    studentThirdSemCGPA = Column(Float)
    studentFourthSemCGPA = Column(Float)
    studentFifthSemCGPA = Column(Float)
    studentSixthSemCGPA = Column(Float)
    studentSeventhSemCGPA = Column(Float)
    studentEightthSemGCPA = Column(Float)
    studentAvgCGPA = Column(Float)
    studentAvgSGPA = Column(Float)
    studentisDiploma = Column(Boolean)
    studentDiplomaMarks = Column(Float)
    studentisBacklog = Column(Boolean)
    studentNumberOfBacklogs = Column(Integer)
    studentActiveBacklog = Column(Integer)
    studentPassiveBacklog = Column(Integer)
    studentisYD = Column(Boolean)
    studentYDYears = Column(Integer)
    studentisEducationGap = Column(Boolean)
    studentEducationGapYears = Column(Integer)
    studentGraduationYear = Column(Date)
    studentisGraduated = Column(Boolean)
    studentUniversityName = Column(String(50))

    studentdetail = relationship('Studentdetail')

    def __init__(self,
                 studentExId=0,
                 studentExStudentId=0,
                 studentTenthCGPA=0,
                 studentTwelfthCGPA=0,
                 studentTenthPercentage=0,
                 studentTwelfthPercentage=0,
                 studentFirstSemCGPA=0,
                 studentSecondSemCGPA=0,
                 studentThirdSemCGPA=0,
                 studentFourthSemCGPA=0,
                 studentFifthSemCGPA=0,
                 studentSixthSemCGPA=0,
                 studentSeventhSemCGPA=0,
                 studentEightthSemGCPA=0,
                 studentAvgCGPA=0,
                 studentAvgSGPA=0,
                 studentisDiploma=False,
                 studentDiplomaMarks=0,
                 studentisBacklog=False,
                 studentNumberOfBacklogs=0,
                 studentActiveBacklog=0,
                 studentPassiveBacklog=0,
                 studentisYD=False,
                 studentYDYears=0,
                 studentisEducationGap=0,
                 studentEducationGapYears=0,
                 studentGraduationYear=1000,
                 studentisGraduated=False,
                 studentUniversityName="DefaultstudentUniversityName"):
        self.__studentExId = 0,
        self.__studentExStudentId = studentExStudentId,
        self.__studentTenthCGPA = studentTenthCGPA,
        self.__studentTwelfthCGPA = studentTwelfthCGPA,
        self.__studentTenthPercentage = studentTenthPercentage,
        self.__studentTwelfthPercentage = studentTwelfthPercentage,
        self.__studentFirstSemCGPA = studentFirstSemCGPA,
        self.__studentSecondSemCGPA = studentSecondSemCGPA,
        self.__studentThirdSemCGPA = studentThirdSemCGPA,
        self.__studentFourthSemCGPA = studentFourthSemCGPA,
        self.__studentFifthSemCGPA = studentFifthSemCGPA,
        self.__studentSixthSemCGPA = studentSixthSemCGPA,
        self.__studentSeventhSemCGPA = studentSeventhSemCGPA,
        self.__studentEightthSemGCPA = studentEightthSemGCPA,
        self.__studentAvgCGPA = studentAvgCGPA,
        self.__studentAvgSGPA = studentAvgSGPA,
        self.__studentisDiploma = studentisDiploma,
        self.__studentDiplomaMarks = studentDiplomaMarks,
        self.__studentisBacklog = studentisBacklog,
        self.__studentNumberOfBacklogs = studentNumberOfBacklogs,
        self.__studentActiveBacklog = studentActiveBacklog,
        self.__studentPassiveBacklog = studentPassiveBacklog,
        self.__studentisYD = studentisYD,
        self.__studentYDYears = studentYDYears,
        self.__studentisEducationGap = studentisEducationGap,
        self.__studentEducationGapYears = studentEducationGapYears,
        self.__studentGraduationYear = studentGraduationYear,
        self.__studentisGraduated = studentisGraduated,
        self.__studentUniversityName = studentUniversityName

    def __repr__(self):
        reprString = """
           Student Details Extended Object:
           StudentEx Id: {}
           StudentEx Student Id: {}
           """.format(self.studentExId, self.studentExStudentId)
        return reprString

    #
    # # ============================================
    # # =========== GETTERS AND SETTERS ============
    # # ============================================
    #
    # # property --> studentExStudentId
    # @property
    # def studentExStudentId(self):
    #     return self.__studentExStudentId
    #
    # @studentExStudentId.setter
    # def studentExStudentId(self, studentExStudentId):
    #     self.__studentExStudentId = studentExStudentId
    #
    # @studentExStudentId.deleter
    # def studentExStudentId(self):
    #     del self.__studentExStudentId
    #
    # # property --> studentTenthCGPA
    # @property
    # def studentTenthCGPA(self):
    #     return self.__studentTenthCGPA
    #
    # @studentTenthCGPA.setter
    # def studentTenthCGPA(self, studentTenthCGPA):
    #     self.__studentTenthCGPA = studentTenthCGPA
    #
    # @studentTenthCGPA.deleter
    # def studentTenthCGPA(self):
    #     del self.__studentTenthCGPA
    #
    # # property --> studentTwelfthCGPA
    # @property
    # def studentTwelfthCGPA(self):
    #     return self.__studentTwelfthCGPA
    #
    # @studentTwelfthCGPA.setter
    # def studentTwelfthCGPA(self, studentTwelfthCGPA):
    #     self.__studentTwelfthCGPA = studentTwelfthCGPA
    #
    # @studentTwelfthCGPA.deleter
    # def studentTwelfthCGPA(self):
    #     del self.__studentTwelfthCGPA
    #
    # # property --> studentTenthPercentage
    # @property
    # def studentTenthPercentage(self):
    #     return self.__studentTenthPercentage
    #
    # @studentTenthPercentage.setter
    # def studentTenthPercentage(self, studentTenthPercentage):
    #     self.__studentTenthPercentage = studentTenthPercentage
    #
    # @studentTenthPercentage.deleter
    # def studentTenthPercentage(self):
    #     del self.__studentTenthPercentage
    #
    # # property --> studentTwelfthPercentage
    # @property
    # def studentTwelfthPercentage(self):
    #     return self.__studentTwelfthPercentage
    #
    # @studentTwelfthPercentage.setter
    # def studentTwelfthPercentage(self, studentTwelfthPercentage):
    #     self.__studentTwelfthPercentage = studentTwelfthPercentage
    #
    # @studentTwelfthPercentage.deleter
    # def studentTwelfthPercentage(self):
    #     del self.__studentTwelfthPercentage
    #
    # # property --> studentFirstSemCGPA
    # @property
    # def studentFirstSemCGPA(self):
    #     return self.__studentFirstSemCGPA
    #
    # @studentFirstSemCGPA.setter
    # def studentFirstSemCGPA(self, studentFirstSemCGPA):
    #     self.__studentFirstSemCGPA = studentFirstSemCGPA
    #
    # @studentFirstSemCGPA.deleter
    # def studentFirstSemCGPA(self):
    #     del self.__studentFirstSemCGPA
    #
    # # property --> studentSecondSemCGPA
    # @property
    # def studentSecondSemCGPA(self):
    #     return self.__studentSecondSemCGPA
    #
    # @studentSecondSemCGPA.setter
    # def studentSecondSemCGPA(self, studentSecondSemCGPA):
    #     self.__studentSecondSemCGPA = studentSecondSemCGPA
    #
    # @studentSecondSemCGPA.deleter
    # def studentSecondSemCGPA(self):
    #     del self.__studentSecondSemCGPA
    #
    # # property --> studentThirdSemCGPA
    # @property
    # def studentThirdSemCGPA(self):
    #     return self.__studentThirdSemCGPA
    #
    # @studentThirdSemCGPA.setter
    # def studentThirdSemCGPA(self, studentThirdSemCGPA):
    #     self.__studentThirdSemCGPA = studentThirdSemCGPA
    #
    # @studentThirdSemCGPA.deleter
    # def studentThirdSemCGPA(self):
    #     del self.__studentThirdSemCGPA
    #
    # # property --> studentFourthSemCGPA
    # @property
    # def studentFourthSemCGPA(self):
    #     return self.__studentFourthSemCGPA
    #
    # @studentFourthSemCGPA.setter
    # def studentFourthSemCGPA(self, studentFourthSemCGPA):
    #     self.__studentFourthSemCGPA = studentFourthSemCGPA
    #
    # @studentFourthSemCGPA.deleter
    # def studentFourthSemCGPA(self):
    #     del self.__studentFourthSemCGPA
    #
    # # property --> studentFifthSemCGPA
    # @property
    # def studentFifthSemCGPA(self):
    #     return self.__studentFifthSemCGPA
    #
    # @studentFifthSemCGPA.setter
    # def studentFifthSemCGPA(self, studentFifthSemCGPA):
    #     self.__studentFifthSemCGPA = studentFifthSemCGPA
    #
    # @studentFifthSemCGPA.deleter
    # def studentFifthSemCGPA(self):
    #     del self.__studentFifthSemCGPA
    #
    # # property --> studentSixthSemCGPA
    # @property
    # def studentSixthSemCGPA(self):
    #     return self.__studentSixthSemCGPA
    #
    # @studentSixthSemCGPA.setter
    # def studentSixthSemCGPA(self, studentSixthSemCGPA):
    #     self.__studentSixthSemCGPA = studentSixthSemCGPA
    #
    # @studentSixthSemCGPA.deleter
    # def studentSixthSemCGPA(self):
    #     del self.__studentSixthSemCGPA
    #
    # # property --> studentSeventhSemCGPA
    # @property
    # def studentSeventhSemCGPA(self):
    #     return self.__studentSeventhSemCGPA
    #
    # @studentSeventhSemCGPA.setter
    # def studentSeventhSemCGPA(self, studentSeventhSemCGPA):
    #     self.__studentSeventhSemCGPA = studentSeventhSemCGPA
    #
    # @studentSeventhSemCGPA.deleter
    # def studentSeventhSemCGPA(self):
    #     del self.__studentSeventhSemCGPA
    #
    # # property --> studentEightthSemGCPA
    # @property
    # def studentEightthSemGCPA(self):
    #     return self.__studentEightthSemGCPA
    #
    # @studentEightthSemGCPA.setter
    # def studentEightthSemGCPA(self, studentEightthSemGCPA):
    #     self.__studentEightthSemGCPA = studentEightthSemGCPA
    #
    # @studentEightthSemGCPA.deleter
    # def studentEightthSemGCPA(self):
    #     del self.__studentEightthSemGCPA
    #
    # # property --> studentAvgCGPA
    # @property
    # def studentAvgCGPA(self):
    #     return self.__studentAvgCGPA
    #
    # @studentAvgCGPA.setter
    # def studentAvgCGPA(self, studentAvgCGPA):
    #     self.__studentAvgCGPA = studentAvgCGPA
    #
    # @studentAvgCGPA.deleter
    # def studentAvgCGPA(self):
    #     del self.__studentAvgCGPA
    #
    # # property --> studentAvgSGPA
    # @property
    # def studentAvgSGPA(self):
    #     return self.__studentAvgSGPA
    #
    # @studentAvgSGPA.setter
    # def studentAvgSGPA(self, studentAvgSGPA):
    #     self.__studentAvgSGPA = studentAvgSGPA
    #
    # @studentAvgSGPA.deleter
    # def studentAvgSGPA(self):
    #     del self.__studentAvgSGPA
    #
    # # property --> studentisDiploma
    # @property
    # def studentisDiploma(self):
    #     return self.__studentisDiploma
    #
    # @studentisDiploma.setter
    # def studentisDiploma(self, studentisDiploma):
    #     self.__studentisDiploma = studentisDiploma
    #
    # @studentisDiploma.deleter
    # def studentisDiploma(self):
    #     del self.__studentisDiploma
    #
    # # property --> studentDiplomaMarks
    # @property
    # def studentDiplomaMarks(self):
    #     return self.__studentDiplomaMarks
    #
    # @studentDiplomaMarks.setter
    # def studentDiplomaMarks(self, studentDiplomaMarks):
    #     self.__studentDiplomaMarks = studentDiplomaMarks
    #
    # @studentDiplomaMarks.deleter
    # def studentDiplomaMarks(self):
    #     del self.__studentDiplomaMarks
    #
    # # property --> studentisBacklog
    # @property
    # def studentisBacklog(self):
    #     return self.__studentisBacklog
    #
    # @studentisBacklog.setter
    # def studentisBacklog(self, studentisBacklog):
    #     self.__studentisBacklog = studentisBacklog
    #
    # @studentisBacklog.deleter
    # def studentisBacklog(self):
    #     del self.__studentisBacklog
    #
    # # property --> studentNumberOfBacklogs
    # @property
    # def studentNumberOfBacklogs(self):
    #     return self.__studentNumberOfBacklogs
    #
    # @studentNumberOfBacklogs.setter
    # def studentNumberOfBacklogs(self, studentNumberOfBacklogs):
    #     self.__studentNumberOfBacklogs = studentNumberOfBacklogs
    #
    # @studentNumberOfBacklogs.deleter
    # def studentNumberOfBacklogs(self):
    #     del self.__studentNumberOfBacklogs
    #
    # # property --> studentActiveBacklog
    # @property
    # def studentActiveBacklog(self):
    #     return self.__studentActiveBacklog
    #
    # @studentActiveBacklog.setter
    # def studentActiveBacklog(self, studentActiveBacklog):
    #     self.__studentActiveBacklog = studentActiveBacklog
    #
    # @studentActiveBacklog.deleter
    # def studentActiveBacklog(self):
    #     del self.__studentActiveBacklog
    #
    # # property --> studentPassiveBacklog
    # @property
    # def studentPassiveBacklog(self):
    #     return self.__studentPassiveBacklog
    #
    # @studentPassiveBacklog.setter
    # def studentPassiveBacklog(self, studentPassiveBacklog):
    #     self.__studentPassiveBacklog = studentPassiveBacklog
    #
    # @studentPassiveBacklog.deleter
    # def studentPassiveBacklog(self):
    #     del self.__studentPassiveBacklog
    #
    # # property --> studentisYD
    # @property
    # def studentisYD(self):
    #     return self.__studentisYD
    #
    # @studentisYD.setter
    # def studentisYD(self, studentisYD):
    #     self.__studentisYD = studentisYD
    #
    # @studentisYD.deleter
    # def studentisYD(self):
    #     del self.__studentisYD
    #
    # # property --> studentYDYears
    # @property
    # def studentYDYears(self):
    #     return self.__studentYDYears
    #
    # @studentYDYears.setter
    # def studentYDYears(self, studentYDYears):
    #     self.__studentYDYears = studentYDYears
    #
    # @studentYDYears.deleter
    # def studentYDYears(self):
    #     del self.__studentYDYears
    #
    # # property --> studentisEducationGap
    # @property
    # def studentisEducationGap(self):
    #     return self.__studentisEducationGap
    #
    # @studentisEducationGap.setter
    # def studentisEducationGap(self, studentisEducationGap):
    #     self.__studentisEducationGap = studentisEducationGap
    #
    # @studentisEducationGap.deleter
    # def studentisEducationGap(self):
    #     del self.__studentisEducationGap
    #
    # # property --> studentEducationGapYears
    # @property
    # def studentEducationGapYears(self):
    #     return self.__studentEducationGapYears
    #
    # @studentEducationGapYears.setter
    # def studentEducationGapYears(self, studentEducationGapYears):
    #     self.__studentEducationGapYears = studentEducationGapYears
    #
    # @studentEducationGapYears.deleter
    # def studentEducationGapYears(self):
    #     del self.__studentEducationGapYears
    #
    # # property --> studentGraduationYear
    # @property
    # def studentGraduationYear(self):
    #     return self.__studentGraduationYear
    #
    # @studentGraduationYear.setter
    # def studentGraduationYear(self, studentGraduationYear):
    #     self.__studentGraduationYear = studentGraduationYear
    #
    # @studentGraduationYear.deleter
    # def studentGraduationYear(self):
    #     del self.__studentGraduationYear
    #
    # # property --> studentisGraduated
    # @property
    # def studentisGraduated(self):
    #     return self.__studentisGraduated
    #
    # @studentisGraduated.setter
    # def studentisGraduated(self, studentisGraduated):
    #     self.__studentisGraduated = studentisGraduated
    #
    # @studentisGraduated.deleter
    # def studentisGraduated(self):
    #     del self.__studentisGraduated
    #
    # # property --> studentUniversityName
    # @property
    # def studentUniversityName(self):
    #     return self.__studentUniversityName
    #
    # @studentUniversityName.setter
    # def studentUniversityName(self, studentUniversityName):
    #     self.__studentUniversityName = studentUniversityName
    #
    # @studentUniversityName.deleter
    # def studentUniversityName(self):
    #     del self.__studentUniversityName
