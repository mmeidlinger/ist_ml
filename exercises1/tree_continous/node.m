classdef node < handle
    %UNTITLED3 Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
    parent   %parent node
    left
    right%vector of child nodes
    checkvalue %property value of the split
    property_index %which property are we checking
    active = false; %wether the node is active
    data %remaining data to be processed for training
    Nmiss %number of misclassified examples
    y   %class (only applies to leaves)
    end
    
    methods
        function obj = node(Data)
            obj.parent=0;
            obj.left = [];
            obj.right = [];
            obj.checkvalue =[];
            obj.active= false;
            obj.data=Data;
            obj.y = inf;
        end
    end
    
end

