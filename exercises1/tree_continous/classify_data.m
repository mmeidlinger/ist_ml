function [ y_hat ] = classify_data( root, data )

y_hat = inf(size(data,1),1);

for yy=1:length(y_hat)
   y_hat(yy) = classify_sample(root,data(yy,:));
end

end

