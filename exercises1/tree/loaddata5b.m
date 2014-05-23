%% Load Data of Problem 5b (cahnge y^9 from +1 to -1)

%% Training Data
X = [ 0 0 0;
      0 0 0;
      0 1 0;
      0 1 0;
      0 1 1;
      1 0 1;
      1 0 0;
      1 0 1;
      1 1 0];
y = [-1 -1 1 1 1 1 1 1 -1 ].';
D= [X y];

%% Test Data

X = [ 1 1 1;
      0 0 1;
      0 1 0;
      0 1 1];
y = [1 -1 -1 1].';
T= [X y];
