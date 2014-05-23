function [ root ] = train_tree( D )

root = node(D);
root.active=true;

while 1
	active = find_active(root,0);
    if active.active ==false
        break
    else
    active.active=false;
    split_node(active);
    end
end