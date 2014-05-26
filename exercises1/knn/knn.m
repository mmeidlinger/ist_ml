
%% K-Nearest Neighbour
clear

% loaddata5a
% loaddata5b
% T=D; %use tree on Training Data

% Problem 6


D=dlmread('../wine-train.txt');
D = D(:,[2:size(D,2) 1]); %move labels to last column
T=dlmread('../wine-test.txt'); 
T = T(:,[2:size(D,2) 1]); %move labels to last column

K=1:size(T,1);

for kk=1:length(K)
    y_hat = classify_data(D,T,K(kk));
    errors(kk) =  sum( y_hat~= T(:,end));
end

% plot(K,errors,'g'); 
% hold on;
S = [K.',errors.'];
save(['6b_test' '.txt'], 'S', '-ascii');
%     save(['6a_train' '.txt'], 'S', '-ascii');