function  y  = classify_sample( root, sample )

    if ~isempty(root.children)
        for ii=1:length(root.children)
            if sample(root.property_index)== root.children(ii).checkvalue
                % remove the property we already checked
                sample(root.property_index)=[];
                y  = classify_sample( root.children(ii), sample ); 
            end
        end
    else
        y=root.y;
    end
end

