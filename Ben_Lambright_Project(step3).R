                                           ###PART 1: SETTING UP###

library(pROC)

#new dataset that only includes people who have all the required variables and are adults who have likely 
#completed their education
NHANES_MentHlth <- subset(NHANES, !is.na(DaysMentHlthBad) & !is.na(Education) & !is.na(PhysActive) &
                            !is.na(CompHrsDay) & !is.na(MaritalStatus) & !is.na(HHIncome) & Age>=25)
dim(NHANES_MentHlth)
sum(is.na(NHANES_MentHlth$Education))
table(NHANES_MentHlth$Age)
min(NHANES_MentHlth$Age)
max(NHANES_MentHlth$Age)

#defining the variable that means that someone is living a happy life
NHANES_MentHlth$MentHlth <- ifelse(NHANES_MentHlth$DaysMentHlthBad>6, "Not Happy",
                                   ifelse(NHANES_MentHlth$DaysMentHlthBad<=6, "Happy", NA))
table(NHANES_MentHlth$MentHlth, exclude=F)
class(NHANES_MentHlth$MentHlth)
NHANES_MentHlth$MentHlth <- as.factor(NHANES_MentHlth$MentHlth)
class(NHANES_MentHlth$MentHlth)
table(NHANES_MentHlth$MentHlth, exclude=F)


#compressing house hold income into low income, middle income, upper middle and high income according
#to https://www.thebalance.com/definition-of-middle-class-income-4126870
NHANES_MentHlth$HHIncome <- ifelse(NHANES_MentHlth$HHIncome %in% c(" 0-4999", " 5000-9999", "10000-14999", 
                                                                   "15000-19999"), "Below or Near Poverty Level", 
                                   ifelse(NHANES_MentHlth$HHIncome %in% c("20000-24999","25000-34999", "35000-44999"),
                                                          "Low Income", 
                                                          ifelse(NHANES_MentHlth$HHIncome=="45000-54999" |
                                                                   NHANES_MentHlth$HHIncome=="55000-64999" |
                                                                   NHANES_MentHlth$HHIncome=="65000-74999" |
                                                                   NHANES_MentHlth$HHIncome=="75000-99999", 
                                                                 "Middle Class",
                                                                 ifelse(NHANES_MentHlth$HHIncome=="more 99999",
                                                                        "Upper Middle Class and High Income",
                                                                        NA))))
#various tests for the function above
levels(NHANES_MentHlth$HHIncome)
levels(NHANES_MentHlth$HHIncome)
table(NHANES_MentHlth$HHINcome)
class(NHANES_MentHlth$HHIncome)
NHANES_MentHlth$HHIncome <- as.factor(NHANES_MentHlth$HHIncome)
class(NHANES_MentHlth$HHIncome)
(table(NHANES_MentHlth$HHIncome))



                                        ###PART 2: HAPPINESS AS OUTCOME###

#table comparing happiness to levels to education
EducationTable <- table(NHANES_MentHlth$Education, NHANES_MentHlth$MentHlth, exclude=F)
EducationTable
(EducationTable/2278)*100
(EducationTable/450)*100
chi_E <- chisq.test(EducationTable, correct=F)
chi_E
chi_E$observed
chi_E$expected


#table comparing happiness to levels to MaritalStatus
MaritalStatusTable <- table(NHANES_MentHlth$MaritalStatus, NHANES_MentHlth$MentHlth, exclude=F)
MaritalStatusTable
(MaritalStatusTable/2278)*100
(MaritalStatusTable/450)*100
chi_M <- chisq.test(MaritalStatusTable, correct=F)
chi_M
chi_M$observed
chi_M$expected

#table comparing happiness to levels to PhysActive
PhysActiveTable <- table(NHANES_MentHlth$PhysActive, NHANES_MentHlth$MentHlth, exclude=F)
PhysActiveTable
(PhysActiveTable/2278)*100
(PhysActiveTable/450)*100
chi_P <- chisq.test(PhysActiveTable, correct=T)
chi_P
chi_P$observed
chi_P$expected


#table comparing happiness to levels to CompHrsDay
CompHrsDayTable <- table(NHANES_MentHlth$CompHrsDay, NHANES_MentHlth$MentHlth, exclude=F)
CompHrsDayTable
(CompHrsDayTable/2278)*100
(CompHrsDayTable/450)*100
chi_C <- chisq.test(CompHrsDayTable, correct=F)
chi_C
chi_C$observed
chi_C$expected

#table comparing happiness to levels to HHIncome
HHIncomeTable <- table(NHANES_MentHlth$HHIncome, NHANES_MentHlth$MentHlth, exclude=F)
HHIncomeTable
(HHIncomeTable/2278)*100
(HHIncomeTable/450)*100
chi_I <- chisq.test(HHIncomeTable, correct=F)
chi_I
chi_I$observed
chi_I$expected

#comparing the different levels of education to happiness
class(NHANES_MentHlth$Education)
levels(NHANES_MentHlth$Education)
NHANES_MentHlth$MentHlth <- as.factor(NHANES_MentHlth$MentHlth)
class(NHANES_MentHlth$Education)
NHANES_MentHlth$Education <- relevel(NHANES_MentHlth$Education, ref="College Grad")
EducationModel <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$Education, family=binomial(link='logit'),
                      data=NHANES_MentHlth)
summary(EducationModel)
#finding the odds ratio
exp(cbind(coef(EducationModel), confint(EducationModel)))

#comparing types of marital status to happiness
levels(NHANES_MentHlth$MaritalStatus)
NHANES_MentHlth$MaritalStatus <- relevel(NHANES_MentHlth$MaritalStatus, ref="Married")
MaritalStatusModel <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$MaritalStatus, family=binomial(link='logit'),
                          data=NHANES_MentHlth)
summary(MaritalStatusModel)
#finding the odds ratio
exp(cbind(coef(MaritalStatusModel), confint(MaritalStatusModel)))

#comparing whether or not the patient is physicaly active to happiness
levels(NHANES_MentHlth$PhysActive)
NHANES_MentHlth$PhysActive <- relevel(NHANES_MentHlth$PhysActive, ref="Yes")
PhysActiveModel <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$PhysActive, family=binomial(link='logit'),
                       data=NHANES_MentHlth)
summary(PhysActiveModel)
#finding the odds ratio
exp(cbind(coef(PhysActiveModel), confint(PhysActiveModel)))

#comparing comparing the amount of time the patient spends on the computer to happiness
levels(NHANES_MentHlth$CompHrsDay)
NHANES_MentHlth$CompHrsDay <- relevel(NHANES_MentHlth$CompHrsDay, ref="1_hr")
CompHrsDayModel <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$CompHrsDay, family=binomial(link='logit'),
                       data=NHANES_MentHlth)
summary(CompHrsDayModel)
#finding the odds ratio
exp(cbind(coef(CompHrsDayModel), confint(CompHrsDayModel)))

#comparing comparing household income to happiness
levels(NHANES_MentHlth$HHIncome)
NHANES_MentHlth$HHIncome <- relevel(NHANES_MentHlth$HHIncome, ref="Below or Near Poverty Level")
HHIncomeModel <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$HHIncome, family=binomial(link='logit'),
                       data=NHANES_MentHlth)
summary(HHIncomeModel)
#finding the odds ratio
exp(cbind(coef(HHIncomeModel), confint(HHIncomeModel)))

#model comparing all of the variables to happiness
UberModel <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$Education + NHANES_MentHlth$MaritalStatus + 
                    NHANES_MentHlth$PhysActive + NHANES_MentHlth$CompHrsDay + 
                    NHANES_MentHlth$HHIncome, family=binomial(link='logit'), data=NHANES_MentHlth)
summary(UberModel)
#finding the odds ratio
exp(cbind(coef(UberModel), confint(UberModel)))

#UberModel with dichotomous education
UberModel3 <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$Education2 + NHANES_MentHlth$MaritalStatus + 
                    NHANES_MentHlth$PhysActive + NHANES_MentHlth$CompHrsDay + 
                    NHANES_MentHlth$HHIncome, family=binomial(link='logit'), data=NHANES_MentHlth)
summary(UberModel3)
#finding the odds ratio
exp(cbind(coef(UberModel3), confint(UberModel3)))



                                            ###PART 3: EDUCATION AS OUTCOME###

#making education dichotomous
levels(NHANES_MentHlth$Education)
NHANES_MentHlth$Education2 <- ifelse(NHANES_MentHlth$Education=="8th Grade" | 
                                       NHANES_MentHlth$Education=="9 - 11th Grade" |
                                       NHANES_MentHlth$Education=="High School",
                                     "Little Education",
                                     ifelse(NHANES_MentHlth$Education=="College Grad" | 
                                              NHANES_MentHlth$Education=="Some College",
                                            "Highly Educated", NA))
table(NHANES_MentHlth$Education2)
class(NHANES_MentHlth$Education2)
NHANES_MentHlth$Education2 <- as.factor(NHANES_MentHlth$Education2)
class(NHANES_MentHlth$Education2)

#table comparing education to levels to MaritalStatus
MaritalStatusTable2 <- table(NHANES_MentHlth$MaritalStatus, NHANES_MentHlth$Education2, exclude=F)
MaritalStatusTable2
(MaritalStatusTable2/1773)*100
(MaritalStatusTable2/955)*100
chi_M2 <- chisq.test(MaritalStatusTable2, correct=F)
chi_M2
chi_M2$observed
chi_M2$expected

#table comparing education to levels to PhysActive
PhysActiveTable2 <- table(NHANES_MentHlth$PhysActive, NHANES_MentHlth$Education2, exclude=F)
PhysActiveTable2
(PhysActiveTable2/1773)*100
(PhysActiveTable2/955)*100
chi_P2 <- chisq.test(PhysActiveTable2, correct=T)
chi_P2
chi_P2$observed
chi_P2$expected

#table comparing education to levels to CompHrsDay
CompHrsDayTable2 <- table(NHANES_MentHlth$CompHrsDay, NHANES_MentHlth$Education2, exclude=F)
CompHrsDayTable2
(CompHrsDayTable2/1773)*100
(CompHrsDayTable2/955)*100
chi_C2 <- chisq.test(CompHrsDayTable2, correct=F)
chi_C2
chi_C2$observed
chi_C2$expected

#table comparing education to levels to HHIncome
HHIncomeTable2 <- table(NHANES_MentHlth$HHIncome, NHANES_MentHlth$Education2, exclude=F)
HHIncomeTable2
(HHIncomeTable2/1773)*100
(HHIncomeTable2/955)*100
chi_I2 <- chisq.test(HHIncomeTable2, correct=F)
chi_I2
chi_I2$observed
chi_I2$expected



                                             ###PART 4: ACCURACY TESTING###

#Accuracy of UberModel using ROC curve
roc_MentHlth <- roc(UberModel$y, UberModel$fitted, ci=T, plot=T, print.auc=T)
roc_MentHlth

#Accuracy of Education using ROC curve
roc_Ed <- roc(EducationModel$y, EducationModel$fitted, ci=T, plot=T, print.auc=T)
roc_Ed

#Accuracy of Happiness versus education and all of its directly related confounders using ROC curve
UberModel2 <- glm(NHANES_MentHlth$MentHlth ~ NHANES_MentHlth$Education + 
                   NHANES_MentHlth$PhysActive + NHANES_MentHlth$CompHrsDay + 
                   NHANES_MentHlth$HHIncome, family=binomial(link='logit'), data=NHANES_MentHlth)
summary(UberModel2)
roc_MentHlth2 <- roc(UberModel2$y, UberModel2$fitted, ci=T, plot=T, print.auc=T)
roc_MentHlth2
