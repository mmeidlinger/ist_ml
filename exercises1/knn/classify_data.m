function y_hat =  classify_data(D,T,k)
    y_hat= inf(size(T,1),1);
    %calculate distance
    d= zeros(size(D,1),1);
    
    for tt=1:size(T,1)
        d = sqrt(sum(abs(D(:,1:end-1) - repmat(T(tt,1:end-1), [size(D,1) 1])).^2,2));
        [d_sorted, ind] = sort(d,'ascend');
        y_hat(tt) =  mode( D(ind(1:k)  , end));
    end

end