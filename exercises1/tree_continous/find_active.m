function [ active_node ] = find_active( root, Nmiss )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

% root.active=false;
% active_node=root;
active_node=root;

if ~isempty(root.left)
    active_node_temp =  find_active(root.left,Nmiss);
    if active_node_temp.Nmiss> Nmiss && active_node_temp.active
        Nmiss = active_node_temp.Nmiss;
        active_node = active_node_temp;
    end
end

if ~isempty(root.right)
    active_node_temp =  find_active(root.right,Nmiss);
    if active_node_temp.Nmiss> Nmiss && active_node_temp.active
        Nmiss = active_node_temp.Nmiss;
        active_node = active_node_temp;
    end
end

end

