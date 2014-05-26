clear;

% Decision tree

loaddata5a
% loaddata5b
% T=D; %use tree on Training Data

% Problem 6


% D=dlmread('../wine-train.txt');
% D = D(:,[2:size(D,2) 1]); %move labels to last column
% T=dlmread('../wine-train.txt'); 
% T = T(:,[2:size(D,2) 1]); %move labels to last column


%% Tree structure
evolve=true;
root= train_tree(D);
y_hat = classify_data(root,T);
errors =  sum( y_hat~= T(:,end));


[N_nodes, errors] = errors_over_complexity(D,T);

plot(N_nodes,errors,'g'); 
hold on;
S = [N_nodes.',errors.'];
save(['5a1_test' '.txt'], 'S', '-ascii');
%     save(['6a_train' '.txt'], 'S', '-ascii');

