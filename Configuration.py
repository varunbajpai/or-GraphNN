#CONFIGURATION VARIABLES
TRAIN_DATAFILE_PATH = 'Data/cell2celltrain.csv'
DEPENDENT_VAR = 'Churn'
PROCESSED_FILE_PATH = 'Data/Train.csv'
TRAINING_EPOCHS = 2000
LEARNING_RATE = 0.001
COSINE_SIMILARITY_MODEl = 'Models/CosineSimilarityModel.torch'

CAT_VAR = ['ServiceArea','ChildrenInHH','HandsetRefurbished','HandsetWebCapable','TruckOwner',
                        'RVOwner','Homeownership','BuysViaMailOrder','RespondsToMailOffers','OptOutMailings',
                        'NonUSTravel','OwnsComputer','HasCreditCard','NewCellphoneUser','NotNewCellphoneUser',
                         'OwnsMotorcycle', 'MadeCallToRetentionTeam', 'CreditRating', 'PrizmCode', 'Occupation',
                         'MaritalStatus'
                        ]

CONT_VAR = ['MonthlyRevenue','MonthlyMinutes','TotalRecurringCharge','DirectorAssistedCalls',
                       'OverageMinutes','RoamingCalls','PercChangeMinutes','PercChangeRevenues',
                       'DroppedCalls','BlockedCalls','UnansweredCalls','CustomerCareCalls','ThreewayCalls',
                       'ReceivedCalls','OutboundCalls','InboundCalls','PeakCallsInOut','OffPeakCallsInOut',
                       'DroppedBlockedCalls','CallForwardingCalls','CallWaitingCalls','MonthsInService',
                       'UniqueSubs','ActiveSubs','Handsets','CurrentEquipmentDays',
                       'AgeHH1','AgeHH2','RetentionCalls','RetentionOffersAccepted','ReferralsMadeBySubscriber',
                       'IncomeGroup', 'AdjustmentsToCreditRating','HandsetPrice','HandsetModels'
                       ]

SIMILARITY_THRESHOLD = 15
NUMBER_OF_ROWS=5


FEATURE_LIST = ['MaritalStatus', 'Occupation']


ALLOWED_COLUMN_NAMES = ['MonthlyRevenue', 'MonthlyMinutes', 'TotalRecurringCharge', 'DirectorAssistedCalls', 'OverageMinutes', 'RoamingCalls', 'PercChangeMinutes', 'PercChangeRevenues', 'DroppedCalls', 'BlockedCalls', 'UnansweredCalls', 'CustomerCareCalls', 'ThreewayCalls', 'ReceivedCalls', 'OutboundCalls', 'InboundCalls', 'PeakCallsInOut', 'OffPeakCallsInOut', 'DroppedBlockedCalls', 'CallForwardingCalls', 'CallWaitingCalls', 'MonthsInService', 'UniqueSubs', 'ActiveSubs', 'Handsets', 'HandsetModels', 'CurrentEquipmentDays', 'AgeHH1', 'AgeHH2', 'RetentionCalls', 'RetentionOffersAccepted', 'ReferralsMadeBySubscriber', 'IncomeGroup', 'AdjustmentsToCreditRating', 'HandsetPrice', 'ServiceArea_AIR', 'ServiceArea_APC', 'ServiceArea_ATH', 'ServiceArea_ATL', 'ServiceArea_AWI', 'ServiceArea_BIR', 'ServiceArea_BOS', 'ServiceArea_CHI', 'ServiceArea_DAL', 'ServiceArea_DEN', 'ServiceArea_DET', 'ServiceArea_FLN', 'ServiceArea_GCW', 'ServiceArea_HAR', 'ServiceArea_HOU', 'ServiceArea_HWI', 'ServiceArea_IND', 'ServiceArea_INH', 'ServiceArea_INU', 'ServiceArea_IPM', 'ServiceArea_KCY', 'ServiceArea_LAU', 'ServiceArea_LAW', 'ServiceArea_LAX', 'ServiceArea_LOU', 'ServiceArea_MIA', 'ServiceArea_MIL', 'ServiceArea_MIN', 'ServiceArea_NCR', 'ServiceArea_NEV', 'ServiceArea_NMC', 'ServiceArea_NMX', 'ServiceArea_NNY', 'ServiceArea_NOL', 'ServiceArea_NOR', 'ServiceArea_NSH', 'ServiceArea_NVU', 'ServiceArea_NYC', 'ServiceArea_OHH', 'ServiceArea_OHI', 'ServiceArea_OKC', 'ServiceArea_OMA', 'ServiceArea_PHI', 'ServiceArea_PHX', 'ServiceArea_PIT', 'ServiceArea_SAN', 'ServiceArea_SDA', 'ServiceArea_SEA', 'ServiceArea_SEW', 'ServiceArea_SFR', 'ServiceArea_SFU', 'ServiceArea_SHE', 'ServiceArea_SLC', 'ServiceArea_SLU', 'ServiceArea_STL', 'ServiceArea_VAH', 'ChildrenInHH_No', 'ChildrenInHH_Yes', 'HandsetRefurbished_No', 'HandsetRefurbished_Yes', 'HandsetWebCapable_No', 'HandsetWebCapable_Yes', 'TruckOwner_No', 'TruckOwner_Yes', 'RVOwner_No', 'RVOwner_Yes', 'Homeownership_Known', 'Homeownership_Unknown', 'BuysViaMailOrder_No', 'BuysViaMailOrder_Yes', 'RespondsToMailOffers_No', 'RespondsToMailOffers_Yes', 'OptOutMailings_No', 'OptOutMailings_Yes', 'NonUSTravel_No', 'NonUSTravel_Yes', 'OwnsComputer_No', 'OwnsComputer_Yes', 'HasCreditCard_No', 'HasCreditCard_Yes', 'NewCellphoneUser_No', 'NewCellphoneUser_Yes', 'NotNewCellphoneUser_No', 'NotNewCellphoneUser_Yes', 'OwnsMotorcycle_No', 'OwnsMotorcycle_Yes', 'MadeCallToRetentionTeam_No', 'MadeCallToRetentionTeam_Yes', 'CreditRating_1-Highest', 'CreditRating_2-High', 'CreditRating_3-Good', 'CreditRating_4-Medium', 'CreditRating_5-Low', 'CreditRating_6-VeryLow', 'CreditRating_7-Lowest', 'PrizmCode_Other', 'PrizmCode_Rural', 'PrizmCode_Suburban', 'PrizmCode_Town', 'Occupation_Clerical', 'Occupation_Crafts', 'Occupation_Homemaker', 'Occupation_Other', 'Occupation_Professional', 'Occupation_Retired', 'Occupation_Self', 'Occupation_Student', 'MaritalStatus_No', 'MaritalStatus_Unknown', 'MaritalStatus_Yes']
