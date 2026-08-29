import React from 'react';

const AlertPanel = ({ threat }) => {
    if (!threat) return null;

    return (
        <div style={{ border: '1px solid #ff4d4f', padding: '15px', borderRadius: '6px', marginTop: '20px', backgroundColor: '#fff2f0' }}>
            <h3>Threat Analysis Report</h3>
            <p><strong>ID:</strong> {threat.id}</p>
            <p><strong>Reason:</strong> {threat.reason}</p>
            <p><strong>Agent Generated Report:</strong></p>
            <pre style={{ whiteSpace: 'pre-wrap', background: '#ffffff', padding: '10px', border: '1px solid #d9d9d9' }}>
                {threat.report || "No AI Crew Report generated."}
            </pre>
        </div>
    );
};

export default AlertPanel;