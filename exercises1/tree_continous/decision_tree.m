clear;

% Decision tree
%% Problem 5 

% loaddata5a;   % Problem 5
% 
% loaddata5b;   % Problem 5 with y9=-1

%% Problem 6

% I think the tree works, it produces 0 error on the training data. However,
% It seems that the wine data set is not discrete -> Not suited for a decision tree 
% (unless we would have decision treshholds as in problem 3a.


D=dlmread('../wine-train.txt');
D = D(:,[2:size(D,2) 1]); %move labels to last column
T=dlmread('../wine-test.txt'); 
T = T(:,[2:size(D,2) 1]); %move labels to last column


%% Tree structure

root= train_tree(D);
y_hat = classify_data(root,T);

errors =  sum( y_hat~= T(:,end))
