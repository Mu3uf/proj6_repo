import React from 'react';

const RiskBadge = ({ level }) => {
    const getColorClass = (risk) => {
        switch (risk) {
            case 'Critical': return '#ff4d4f';
            case 'High': return '#ff7a45';
            case 'Medium': return '#ffa940';
            case 'Low': return '#52c41a';
            default: return '#d9d9d9';
        }
    };

    const style = {
        backgroundColor: getColorClass(level),
        color: '#ffffff',
        padding: '4px 8px',
        borderRadius: '4px',
        fontWeight: 'bold',
        fontSize: '12px',
        display: 'inline-block'
    };

    return <span style={style}>{level}</span>;
};

export default RiskBadge;