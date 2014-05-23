function  y  = classify_sample( root, sample )

    if ~isempty(root.children)
            if sample(root.property_index)>= root.checkvalue
                y  = classify_sample( root.children(1), sample ); 
            else
                y  = classify_sample( root.children(2), sample );
            end
    else
        y=root.y;
    end
end

