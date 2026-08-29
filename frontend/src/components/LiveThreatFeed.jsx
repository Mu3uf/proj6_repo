import React from 'react';

const LiveThreatFeed = ({ liveEvents }) => {
    return (
        <div style={{ border: '1px solid #ccc', padding: '10px', borderRadius: '6px', maxHeight: '150px', overflowY: 'auto', marginBottom: '20px' }}>
            <h4>WebSocket Real-time Feed</h4>
            {liveEvents.length === 0 ? <p>No live stream data...</p> : (
                <ul>
                    {liveEvents.map((e, index) => (
                        <li key={index}>
                            [{e.timestamp}] {e.source_ip} -&gt; {e.classification} ({e.risk_level})
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default LiveThreatFeed;