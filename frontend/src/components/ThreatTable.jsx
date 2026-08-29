import React from 'react';
import RiskBadge from './RiskBadge';

const ThreatTable = ({ threats, onSelectThreat }) => {
    return (
        <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '10px' }}>
            <thead>
                <tr style={{ borderBottom: '2px solid #ccc', textAlign: 'left' }}>
                    <th>Timestamp</th>
                    <th>Source IP</th>
                    <th>Destination IP</th>
                    <th>Classification</th>
                    <th>Score</th>
                    <th>Risk Level</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {threats.map((t) => (
                    <tr key={t.id} style={{ borderBottom: '1px solid #eee' }}>
                        <td>{t.timestamp}</td>
                        <td>{t.source_ip}</td>
                        <td>{t.destination_ip}</td>
                        <td>{t.classification}</td>
                        <td>{t.anomaly_score}</td>
                        <td><RiskBadge level={t.risk_level} /></td>
                        <td>
                            <button onClick={() => onSelectThreat(t)}>View Report</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default ThreatTable;