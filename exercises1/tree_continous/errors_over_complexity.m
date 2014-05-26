function [ N_nodes, errors ] = errors_over_complexity( D,T)

root = node(D);
root.active=true;
rr=1;
while 1
    y_hat=classify_data( root, T );
    errors(rr) =  sum( y_hat~= T(:,end));
    N_nodes(rr)= count_nodes(root);
	active = find_active(root,0);
    if active.active ==false
        break
    else
    active.active=false;
    split_node(active);
    end
    rr=rr+1;
end


