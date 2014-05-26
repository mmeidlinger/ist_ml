function split_node( root )


%% Check which property to split along
for pp=1:size(root.data,2)-1    %iterate over properties
    % check what property values there are
    values=root.data(:,pp);
%     for vv=1:length(values)
%         split_labels_left=root.data(root.data(:,pp)>=values(vv),end);
%         maj_vote_left(vv,pp)=mode(split_labels_left);
%         accuracies_left(vv,pp)= sum(split_labels_left==maj_vote_left(vv,pp));
%         
%         split_labels_right=root.data(root.data(:,pp)<values(vv),end);
%         maj_vote_right(vv,pp)=mode(split_labels_right);
%         accuracies_right(vv,pp)= sum(split_labels_right==maj_vote_right(vv,pp));
%     end
        vv=1;
        split_labels_left=root.data(root.data(:,pp)>=mean(values),end);
        maj_vote_left(vv,pp)=mode(split_labels_left);
        accuracies_left(vv,pp)= sum(split_labels_left==maj_vote_left(vv,pp));
        
        split_labels_right=root.data(root.data(:,pp)<mean(values),end);
        maj_vote_right(vv,pp)=mode(split_labels_right);
        accuracies_right(vv,pp)= sum(split_labels_right==maj_vote_right(vv,pp));
end
[~,ind] = max(accuracies_left(:)+accuracies_right(:));
[vv_max,pp_max] = ind2sub(size(accuracies_left),ind);
%% Perform (binary) split: left = \beg than threshold, right= < than threshold
theta= mean(root.data(:,pp_max));
split_data_left = root.data(root.data(:,pp_max)>=theta,:);
split_data_right = root.data(root.data(:,pp_max)< theta,:);

if ~isempty(split_data_left) && ~isempty(split_data_right)
    left_child = node(split_data_left); 
    left_child.parent=root;
    left_child.Nmiss = size(split_data_left,1)-accuracies_left(vv_max,pp_max);
    if left_child.Nmiss ==0 
        left_child.y = maj_vote_left(vv_max,pp_max);
    else
        left_child.active=true;
    end

    right_child = node(split_data_right); 
    right_child.parent=root;
    right_child.Nmiss = size(split_data_right,1)-accuracies_right(vv_max,pp_max);
    if right_child.Nmiss ==0 
        right_child.y = maj_vote_right(vv_max,pp_max);
    else
        right_child.active=true;
    end
else
    right_child = [];
    left_child = [];
end

root.left= left_child;
root.right= right_child;
root.property_index = pp_max;
root.checkvalue=theta;
root.data=[];