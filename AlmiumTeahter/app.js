const dictGraphUnfilter = {"Retrieve": ["DecisionTree", "LinearRegression", "Neural Net", "NearestNeighbors", "NaiveBayes", "JMySVMLearner", "MyKLRLearner", "FrequencyDiscretization", "Bagging", "MissingValueReplenishment", "DecisionTree", "Preprocessing", "NoiseGenerator", "Cross Validation", "Tree2RuleConverter", "Cross Validation", "Nominal2Binominal", "Normalize", "IdTagging", "Sampling", "FrequencyDiscretization", "MinimalEntropyPartitioning", "ExampleFilter", "Preprocessing", "NoiseGenerator", "RemoveCorrelatedFeatures", "Generation", "NominalFeatureIterator", "IdTagging", "MissingValueReplenishment", "JMySVMLearner", "Cross Validation", "MissingValueReplenishment", "Cross Validation", "SimpleValidation", "Validation", "ModelApplier", "Cross Validation", "RemoveCorrelatedFeatures", "RemoveUselessAttributes", "Normalization", "PCA", "GHA", "FastICA", "PCA", "Relief", "FS", "PCAWeighting", "EvolutionaryWeighting", "InitialWeights", "YAGGA", "AttributeConstructionsLoader", "IdTagging", "ParameterOptimization", "ChiSquaredWeighting", "ANOVAMatrix", "ROCComparator", "Aggregation", "ParameterOptimization", "GridParameterOptimization", "ParameterOptimization", "KMeans", "KMedoids", "AgglomerativeClustering", "Clustering", "KMeans", "KMeans", "KMeans", "ParameterIteration", "TopDownClustering", "Obfuscator"], "FrequencyDiscretization": ["RuleLearner", "Nominal2Binominal"], "MissingValueReplenishment": ["AdaBoost", "DecisionStump", "Cross Validation"], "DecisionTree": ["Apply Model"], "Retrieve (2)": ["Apply Model", "NaiveBayes", "Training (2)"], "Preprocessing": ["FPGrowth"], "FPGrowth": ["AssociationRuleGenerator", "AssociationRuleGenerator"], "TrainingSetGenerator": ["NearestNeighbors", "LibSVMLearner"], "NearestNeighbors": ["TestApplyModel"], "TestSetGenerator": ["TestApplyModel"], "TestApplyModel": ["ThresholdFinder", "Apply Model"], "ThresholdFinder": ["Apply Threshold", "ThresholdApplier", "ThresholdApplier", "ThresholdApplier", "ThresholdApplier"], "ApplySetGenerator": ["Apply Model"], "Apply Model": ["Apply Threshold", "Performance", "Performance"], "Apply Threshold": ["Performance"], "ModelApplier": ["ThresholdFinder", "Performance", "ClassificationPerformance", "ClassificationPerformance", "RegressionPerformance", "ClassificationPerformance", "ClassificationPerformance", "BinominalClassificationPerformance", "Performance", "Performance", "WrapperEvaluation", "RegressionPerformance", "Performance", "RegressionPerformance", "Performance", "Performance", "ClassificationPerformance", "ThresholdFinder", "RegressionPerformance", "Performance", "Performance", "ClassificationPerformance", "Performance", "Performance", "Performance", "ClassificationPerformance", "ThresholdApplier"], "ThresholdApplier": ["Performance", "Performance", "Performance"], "ExampleSetGenerator": ["Cross Validation", "NoiseGenerator", "NoiseGenerator", "Cross Validation", "Stacking", "Vote", "Normalization", "StratifiedSampling", "ExampleSetMerge", "DistanceBasedOutlierDetection", "DiscretizationOnSpecialAttributes", "IdTagging", "IdTagging", "AttributeFilter", "AttributeFilter", "FeatureIterator", "Cross Validation", "Cross Validation", "NoiseGenerator", "IOMultiplier_1", "NoiseGenerator", "ChiSquaredWeighting", "Cross Validation", "NoiseGenerator", "JMySVMLearner", "Cross Validation", "SOMDimensionalityReduction", "RandomOptimizer", "NoiseGenerator", "GridParameterOptimization", "ParameterIteration", "NoiseGenerator", "RandomOptimizer", "SupportVectorClustering", "Normalization", "Cross Validation", "JMySVMLearner"], "Test": ["Performance", "Performance", "Performance", "Evaluation", "Write Special", "Performance", "Performance", "Evaluation", "Evaluation", "Performance", "ClassificationPerformance"], "NoiseGenerator": ["Cross Validation", "Cross Validation", "Cross Validation", "WrapperXValidation", "GeneticAlgorithm", "GeneticAlgorithm", "Normalization", "MultipleLabelIterator", "FeatureSubsetIteration"], "Nominal2Binominal": ["AttributeFilter"], "AttributeFilter": ["FPGrowth", "AttributeSubsetPreprocessing", "AttributeSubsetPreprocessing"], "Normalization": ["PolynomialRegression", "PrincipalComponents", "LearningCurve", "DBScanClustering"], "PolynomialRegression": ["Apply Model", "Apply Model"], "RepositorySource": ["MergeValues", "RemoveUselessAttributes", "NormalizationOnTemperature", "SplittingChain"], "MergeValues": ["Select Attributes"], "Select Attributes": ["ExampleFilter", "ExampleSetJoin", "AttributeConstruction", "AttributeConstruction", "IOStorer (2)"], "NominalFeatureIterator": ["NumericalFeatureIterator"], "NumericalFeatureIterator": ["Decision Tree"], "FirstExampleSetGenerator": ["FirstIdTagging"], "FirstIdTagging": ["ExampleSetJoin"], "SecondExampleSetGenerator": ["SecondIdTagging"], "SecondIdTagging": ["Select Attributes"], "ExampleSetGenerator (2)": ["ExampleSetMerge"], "ExampleSetGenerator (3)": ["ExampleSetMerge"], "DistanceBasedOutlierDetection": ["ExampleFilter"], "NormalizationOnTemperature": ["DiscretizationOnHumidity"], "IOMultiplier": ["FirstFilter", "SecondFilter"], "ExampleFilter": ["Select Attributes", "Select Attributes", "Aggregation", "DataMacroDefinition", "Loop Values"], "AttributeConstruction": ["AttributeSubsetPreprocessing", "AttributeSubsetPreprocessing", "Loop Values"], "AttributeSubsetPreprocessing": ["Mapping", "Mapping", "Sorting", "ChangeAttributeName"], "Mapping": ["ChangeAttributeRole", "ChangeAttributeRole"], "ExampleFilter (2)": ["Select Attributes (2)", "Select Attributes (2)"], "Select Attributes (2)": ["KMeans", "KMeans"], "IdTagging": ["LOFOutlierDetection", "LOFOutlierDetection", "IdToRegular"], "LOFOutlierDetection": ["IOMultiplier_1", "IOMultiplier_1"], "IOMultiplier_1": ["Outliers", "NonOutliers", "Outliers", "NonOutliers", "Cross Validation", "Cross Validation (2)"], "Outliers": ["ExampleSetMerge", "ExampleSetMerge"], "NonOutliers": ["ExampleSetMerge", "ExampleSetMerge"], "IdToRegular": ["Numerical2Polynominal (2)"], "Numerical2Polynominal (2)": ["Aggregate"], "Aggregate": ["Set Role"], "Set Role": ["FP-Growth"], "Aggregation": ["DataMacroDefinition", "AttributeConstruction", "DataMacroDefinition", "AttributeConstruction"], "Generate Data": ["Loop Values", "KernelKMeans"], "Loop Values": ["ExampleSetMerge", "ExampleSetMerge"], "SetData": ["MacroConstruction"], "DataMacroDefinition": ["SingleMacroDefinition", "MacroConstruction"], "SingleMacroDefinition": ["IteratingOperatorChain", "ValueIterator"], "ChangeAttributeName": ["ChangeAttributeName (2)"], "ChangeAttributeName (2)": ["AttributeConstruction"], "ExampleSetMerge": ["Pivot"], "NominalExampleSetGenerator": ["Sample"], "Sample": ["GuessValueTypes"], "ValueIterator": ["Macro2Log"], "Macro2Log": ["ProcessLog"], "IORetriever": ["Select Attributes"], "OperatorChain": ["FeatureIterator"], "FeatureIterator": ["ProcessLog2ExampleSet"], "ProcessLog2ExampleSet": ["ClearProcessLog", "ClearProcessLog"], "ClearProcessLog": ["GuessValueTypes (2)", "IOStorer"], "GuessValueTypes (2)": ["ExampleFilter"], "DecisionStump": ["ModelApplier", "ModelApplier"], "JMySVMLearner": ["ModelApplier", "ModelApplier", "PlattScaling", "PlattScaling"], "Write Special": ["RegressionPerformance"], "NaiveBayes": ["ModelApplier"], "FSModelApplier": ["FSEvaluation"], "FSEvaluation": ["FSMinMaxWrapper"], "ModelApplier (2)": ["RegressionPerformance (2)"], "Cross Validation (2)": ["T-Test"], "Cross Validation": ["T-Test", "ProcessLog", "ProcessLog", "ProcessLog", "Log", "Log", "ProcessLog", "ProcessLog", "ProcessLog "], "T-Test": ["Anova", "Anova"], "LiftParetoChart": ["ModelApplier", "ModelApplier", "IOStorer", "ModelApplier", "ModelApplier", "IOStorer"], "DirectMailingExampleSetGenerator": ["SimpleValidation", "SimpleValidation"], "PCA": ["ModelApplier", "ModelApplier", "ComponentWeights", "ComponentWeights"], "GHA": ["ComponentWeights", "ComponentWeights"], "FastICA": ["ModelApplier", "ModelApplier"], "Relief": ["AttributeWeightSelection", "AttributeWeightSelection"], "Applier": ["Performance", "RegressionPerformance"], "PCAWeighting": ["WeightGuidedFeatureSelection", "WeightGuidedFeatureSelection"], "SimpleValidation": ["ProcessLog", "ProcessLog"], "Selection": ["Cross Validation"], "InitialWeights": ["GridParameterOptimization", "GridParameterOptimization"], "YAGGA": ["AttributeConstructionsWriter", "AttributeWeightsWriter"], "AttributeConstructionsLoader": ["AttributeWeightSelection"], "AttributeWeightsLoader": ["AttributeWeightSelection"], "LibSVMLearner": ["ModelApplier"], "GridSetGenerator": ["ModelApplier"], "Performance": ["ProcessLog"], "ParameterOptimization": ["ParameterSetter"], "ApplierChain": ["ProcessLog"], "MultipleLabelGenerator": ["NoiseGenerator"], "MultipleLabelIterator": ["AverageBuilder"], "OperatorEnabler": ["Cross Validation"], "IteratingPerformanceAverage": ["Log"], "MacroConstruction": ["DecisionTree"], "KMeans": ["SVDReduction", "ClusterCentroidEvaluator", "ClusterCentroidEvaluator", "ClusterModel2ExampleSet", "ClusterModel2ExampleSet", "ChangeAttributeRole", "Evaluation", "Evaluation", "Evaluation", "Evaluation"], "ClusterCentroidEvaluator": ["ProcessLog", "ProcessLog"], "KMedoids": ["SVDReduction"], "Clustering": ["SVDReduction"], "ClusterModel2ExampleSet": ["Cross Validation"], "ChangeAttributeRole": ["DecisionTree"], "Evaluation": ["SVDReduction", "ProcessLog", "ProcessLog"], "Obfuscator": ["DeObfuscator"], "ThresholdCreator": ["ThresholdApplier"], "PlattScaling": ["ModelApplier", "ModelApplier"]}

let uniqueDict={}
for (let elem in dictGraphUnfilter){
  for (let op of dictGraphUnfilter[elem]){
    uniqueDict[op]=[]
  }
}

for (let elem in uniqueDict){
  if (elem in dictGraphUnfilter){
    continue
  }
  else {
    dictGraphUnfilter[elem]=[]
  }
}
const dictGraph=dictGraphUnfilter

const MIN = 2
const MEDIUM = 4
const MAX = 6
let nodes = null;
let edges = null;
let network = null;
let arrowToTyp = {
    to: {
      enabled: true,
      type: "inv_curve",
    },
  }


function dictGraphToNodes(dictGraph){
    let nodes= []
    for (let elem in dictGraph){
        let cpt = 0
        for (let op in dictGraph[elem]){
            if(op == elem){
                cpt=cpt+1
            }
        }
        nodes.push({ id: elem, value: cpt, label:elem })
    }
    return nodes
}


function dictGraphToEdges(dictGraph){
    let edges= []
    for (let elem in dictGraph){
        let dict = {}
        for (let op of dictGraph[elem]){
           // edges.push({ from: elem, to: op, value: 3, title: "3 emails per week",arrows: arrowToTyp })
           if (op in dict){
             dict[op]+=1
           }
           else {
             dict[op]=1}
        }
        for (let elemOP in dict){
          edges.push({ from: elem, to: elemOP, value: dict[elemOP] , title: elem,arrows: arrowToTyp })
        }
    }
    return edges
}

function draw() {
  // create people.
  // value corresponds with the age of the person
  nodes = dictGraphToNodes(dictGraph);

  // create connections between people
  // value corresponds with the amount of contact between two people
  edges = dictGraphToEdges(dictGraph);

  // Instantiate our network object.
  let container = document.getElementById("mynetwork");
  let data = {
    nodes: nodes,
    edges: edges,
  };
  let options = {
    nodes: {
      shape: "dot",
      scaling: {
        label: {
          min: 8,
          max: 20,
        },
      },
    },
  };
  network = new vis.Network(container, data, options);
}


window.addEventListener("load", () => {
  draw();
});
