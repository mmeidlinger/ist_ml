function split_node( root )


%% Check which property to split along
for pp=1:size(root.data,2)-1    %iterate over properties
    % check what property values there are
    values=unique(root.data(:,pp));
    for vv=1:length(values)
        split_labels=root.data(root.data(:,pp)==values(vv),end);
        maj_vote(vv,pp)=mode(split_labels);
        accuracies(vv,pp)= sum(split_labels==maj_vote(vv,pp));
    end
end
[~ , split_property_index] = max(sum(accuracies,1));

%% Perform split
split_values= unique(root.data(:,split_property_index));
for ss=1: length(split_values)
    split_data = root.data(split_values(ss)==root.data(:,split_property_index),:);
    split_data(:,split_property_index)=[];
    new_child = node(split_data); 
    new_child.parent=root;
    new_child.checkvalue= split_values(ss);
    new_child.Nmiss = size(root.data,1)-sum(accuracies(:,split_property_index),1);
    if new_child.Nmiss ~=0
        new_child.active=true;
    else
        new_child.y = maj_vote(ss,split_property_index);
    end
    root.children= [root.children new_child ];
    root.property_index = split_property_index;
end

root.data=[];