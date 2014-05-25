clear;

% Decision tree


% Problem 6


D=dlmread('../wine-train.txt');
D = D(:,[2:size(D,2) 1]); %move labels to last column
T=dlmread('../wine-test.txt'); 
T = T(:,[2:size(D,2) 1]); %move labels to last column


%% Tree structure
root= train_tree(D);
y_hat = classify_data(root,T);
errors =  sum( y_hat~= T(:,end));


%% In this section we iterate over increasingly bigger sets of training data

for dd =1:size(D,1)
    D_subset = D(1:dd,:);
    root= train_tree(D_subset);
    y_hat = classify_data(root,T);
    errors(dd,1) =  sum( y_hat~= T(:,end));
    N_nodes(dd,1) = count_nodes(root);
    clear root;
end

plot(N_nodes,errors)

S = [N_nodes,errors];
save(['6a_test' '.txt'], 'S', '-ascii');
% save(['6a_train' '.txt'], 'S', '-ascii');


