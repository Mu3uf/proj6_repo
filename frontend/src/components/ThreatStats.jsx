import React from 'react';

const ThreatStats = ({ stats }) => {
    const containerStyle = {
        display: 'flex',
        gap: '20px',
        marginBottom: '20px'
    };

    const cardStyle = {
        flex: 1,
        padding: '15px',
        border: '1px solid #ccc',
        borderRadius: '6px',
        textAlign: 'center'
    };

    return (
        <div style={containerStyle}>
            <div style={cardStyle}>
                <h3>Total Threats</h3>
                <p>{stats.total || 0}</p>
            </div>
            <div style={cardStyle}>
                <h3>Critical</h3>
                <p>{stats.critical || 0}</p>
            </div>
            <div style={cardStyle}>
                <h3>High</h3>
                <p>{stats.high || 0}</p>
            </div>
            <div style={cardStyle}>
                <h3>Medium</h3>
                <p>{stats.medium || 0}</p>
            </div>
            <div style={cardStyle}>
                <h3>Low</h3>
                <p>{stats.low || 0}</p>
            </div>
        </div>
    );
};

export default ThreatStats;