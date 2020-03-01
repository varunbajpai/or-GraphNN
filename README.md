##Files and Folder Description

Folders
1) Data  : Contains the Data and the processed data
2) Models : Will contain the models of training


Files
1)  BuildFeatureMappedGraph.ipynb : Builds graphs based on specific features
2)  BuildGraph.ipynb : Builds Graph based on cosine similarity
3)  CosineSimilarity-Train_File.ipynb : Trains the model based on Cosine Similarity Graph
4)  DataPreProcessing.ipynb : For Data Pre-Processing
5)  FeatureSimilarityTrain.ipynb : Trains the models based on similarity among features
6)  GraphNeuralNetwork.ipynb : Defines the model which will be trained
7)  Predict.ipynb : Need to specify the model file from where results can be predicted from
8)  Configuration.py : Contains Data being used as configuration in program
9)  AutoGluOn.ipynb : Contains Multiple Models which use grid search for hyper parameter tuning
10) PrincipalComponentAnalysis(PCA).ipynb : Principal componenet Analysis to find the most representative variaables of data


Best Model:
    Models were tried with 
    
        A) Graph Neural network
        
            a) Cosine Similarity Model : Better model in Graph Neural Network
            
            b) Feature Similarity Model : Not so good as features are taken indivudially (Graph was built using specific features)
            
    
    AutoGluon Models:
    
        Multiple Models are created in AutoGluon for tabular Data
        
        
Average Accuraccy by all classifiers including Graph Neural Network: 74%


PCA : PCA was applied to Continuous but the results with PCA were not good as compared with full dataset, Hence PCA is implementetd but not used, In order to use PCA we need to import the file and pass processed DataFrame into get_columns_from_pca function  

Graph Building Complexity : O(n^2) as every node needs to be mapped with every other node

Running the Files:
Files can be run individually.

For Training based on Cosine Similarity (Recommended):
Run the File: CosineSimilarity-Train_File.ipynb 

For Training based on Feature Similarity (Recommended):
Add the fields to the feature list in the Configuration.py file in the list named : FEATURE_LIST
Run the File: CosineSimilarity-Train_File.ipynb 

For Predicting the results: 
Run the File: Predict.ipynb

Sample Predictions along with sample dataframe is shown in the file
