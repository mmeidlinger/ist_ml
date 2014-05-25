function  y  = classify_sample( root, sample )


if sample(root.property_index)>= root.checkvalue
    if ~isempty(root.left)
        y  = classify_sample( root.left, sample ); 
    else
        y=root.y;
    end
else
    if ~isempty(root.right)
        y  = classify_sample( root.right, sample );
    else
        y=root.y;
    end
end

end

