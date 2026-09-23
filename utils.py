"""
Data iunderstanding is ideally: using the current data to tell a story and discover hidden stoies behind it using only the data
"""


# shape - rows adn columns
# info
# check for missing values
# check for duplicates
# univariate analysis
# bivariate analysis
# mutlivariate analysis
# descriptive stats

class DataUnderstanding:
    #  attributes 
    def __init__(self, df):
        self.df = df 

    # methods/ behaviors
    def getSnippetOfData(self):
        display(self.df.info())
        print("="*20)
        display(self.df.head())

    def getMissingValues(self):
        display(df.isna().sum()* 100 / len(df))

    def getDuplicates(self):
        df_duplicate = self.df[self.df.duplicated(keep=False)]   
        display(f"Data set has {len(df_duplicate)} duplicates")

    def newFeature(self, new_feature, feature_one, feature_two):
        self.df[new_feature] = self.df[feature_one] * self.df[feature_two]


    def univariateAnalysis(self, feature_name, type_is_numerical):
        display(self.df[feature_name].info())
        print("="*20)
        display(self.df[feature_name].describe())

    def bivariateAnalysis(self, feature_one, feature_two):
        display(self.df[[feature_one, feature_two]].describe()) 

    def mutlivariateAnalysis(self):
        display()    
