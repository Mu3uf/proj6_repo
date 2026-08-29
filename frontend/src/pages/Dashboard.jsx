import React, { useState, useEffect } from 'react';
import ThreatStats from '../components/ThreatStats';
import LiveThreatFeed from '../components/LiveThreatFeed';
import ThreatTable from '../components/ThreatTable';
import AlertPanel from '../components/AlertPanel';
import DetectionForm from '../components/DetectionForm';
import { fetchThreats, postDetection } from '../services/threatApi';

const Dashboard = () => {
    const [threats, setThreats] = useState([]);
    const [stats, setStats] = useState({ total: 0, critical: 0, high: 0, medium: 0, low: 0 });
    const [selectedThreat, setSelectedThreat] = useState(null);
    const [liveEvents, setLiveEvents] = useState([]);

    // حساب الإحصائيات تلقائياً من البيانات المتاحة
    const calculateStats = (dataList) => {
        const counts = {
            total: dataList.length,
            critical: 0,
            high: 0,
            medium: 0,
            low: 0
        };
        dataList.forEach(t => {
            const level = (t.risk_level || t.riskLevel || '').toLowerCase();
            if (counts[level] !== undefined) {
                counts[level]++;
            }
        });
        setStats(counts);
    };

    const loadData = async () => {
        try {
            const data = await fetchThreats();
            const list = Array.isArray(data) ? data : [];
            setThreats(list);
            calculateStats(list);
        } catch (err) {
            console.error("Error loading threats:", err);
        }
    };

    useEffect(() => {
        loadData();
        const ws = new WebSocket('ws://127.0.0.1:8000/ws/threats');

        ws.onmessage = (event) => {
            const newThreat = JSON.parse(event.data);
            setLiveEvents(prev => [newThreat, ...prev]);
            setThreats(prev => {
                const updated = [newThreat, ...prev];
                calculateStats(updated);
                return updated;
            });
        };

        return () => ws.close();
    }, []);

    const handleFormSubmit = async (formData) => {
        try {
            const result = await postDetection(formData);
            if (result) {
                setThreats(prev => {
                    const updated = [result, ...prev];
                    calculateStats(updated);
                    return updated;
                });
            }
        } catch (err) {
            console.error("Error submitting event:", err);
        }
    };

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
            <h1>Threat Intelligence Dashboard</h1>
            <ThreatStats stats={stats} />
            <LiveThreatFeed liveEvents={liveEvents} />
            <DetectionForm onSubmit={handleFormSubmit} />
            <ThreatTable threats={threats} onSelectThreat={setSelectedThreat} />
            <AlertPanel threat={selectedThreat} />
        </div>
    );
};

export default Dashboard;