#CONFIGURATION VARIABLES
TRAIN_DATAFILE_PATH = 'Data/cell2celltrain.csv'
DEPENDENT_VAR = 'Churn'
PROCESSED_FILE_PATH = 'Data/Train.csv'
TRAINING_EPOCHS = 2000
LEARNING_RATE = 0.001

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