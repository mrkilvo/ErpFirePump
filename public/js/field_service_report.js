alert('Field Service Report List View Script Loaded');
console.log('Field Service Report List View Script Loaded');

frappe.listview_settings['Field Service Report'] = {
    get_indicator: function(doc) {
        if (doc.defect_type === 'None Critical') {
            return [__('None Critical'), 'orange', 'defect_type,=,None Critical'];
        } else if (doc.defect_type === 'None Conformance') {
            return [__('None Conformance'), 'gray', 'defect_type,=,None Conformance'];
        } else if (doc.defect_type === 'Recommendation') {
            return [__('Recommendation'), 'blue', 'defect_type,=,Recommendation'];
        } else if (doc.defect_type === 'Critical') {
            return [__('Critical'), 'red', 'defect_type,=,Critical'];
        } else if (doc.defect_type === 'Advisory') {
            return [__('Advisory'), 'blue', 'defect_type,=,Advisory'];
        } else {
            return [__('Others'), 'gray', 'defect_type,=,Others'];
        }
    }
};