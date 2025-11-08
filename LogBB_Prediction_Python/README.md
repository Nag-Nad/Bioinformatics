The prediction of blood-barrier permeability parameter with RDkit and machine learning (SKlearn).

•	For the prediction, I used a compiled dataset with 1000 molecules with their corresponding SMILES and the experimentally LogBB values (Shaker et al., 2023) as the training data. This can be accessed here:  http://ssbio.cau.ac.kr/software/logbb_pred/dataset.zip

•	The zinc20 dataset, with approximately 5000 compounds, was also used as the testing data and the corresponding values were predicted accordingly. 

•	The error metrics of the model was measured as: MSE = 0.40

•	For the ML, the random forest algorithm was used because it had a slightly better performance according to the MSE values compared to LightGBM algorithm, which was used in the most recent papers (Shaker et al., 2023; Shaker et al., 2021). 

**Suggestions for the model improvement**: this model could be trained on a larger dataset.  