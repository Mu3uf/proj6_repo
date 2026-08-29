import React, { useState } from 'react';

const DetectionForm = ({ onSubmit }) => {
    const [formData, setFormData] = useState({
        source_ip: '192.168.1.50',
        destination_ip: '10.0.0.1',
        port: 80,
        status: 'DENY',
        request_frequency: 10,
        src_port: 22,
        dst_port: 401,
        event_type: 'LOGIN_ATTEMPT',
        action: 'DENY',
        protocol: 'TCP',
        bytes_sent: 12,
        bytes_received: 255.5,
        duration: 15,
        count: 1,
        srv_count: 1,
        failed_logins: 0,
        unique_ports: 1
    });

    const handleChange = (e) => {
        const { name, value, type } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: type === 'number' ? Number(value) : value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        const payload = {
            ...formData,
            port: Number(formData.port),
            request_frequency: Number(formData.request_frequency),
            src_port: Number(formData.src_port),
            dst_port: Number(formData.dst_port),
            bytes_sent: Number(formData.bytes_sent),
            bytes_received: Number(formData.bytes_received),
            duration: Number(formData.duration),
            count: Number(formData.count),
            srv_count: Number(formData.srv_count),
            failed_logins: Number(formData.failed_logins),
            unique_ports: Number(formData.unique_ports)
        };

        if (onSubmit) {
            await onSubmit(payload);
        }
    };

    return (
        <form onSubmit={handleSubmit} style={{ margin: '20px 0', padding: '15px', border: '1px solid #ccc' }}>
            <h3>Manual Event Detection Form</h3>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                <input name="source_ip" value={formData.source_ip} onChange={handleChange} placeholder="Source IP" />
                <input name="destination_ip" value={formData.destination_ip} onChange={handleChange} placeholder="Destination IP" />
                <input name="port" type="number" value={formData.port} onChange={handleChange} placeholder="Port" />
                <input name="status" value={formData.status} onChange={handleChange} placeholder="Status" />
                <input name="request_frequency" type="number" value={formData.request_frequency} onChange={handleChange} placeholder="Request Frequency" />
                <input name="event_type" value={formData.event_type} onChange={handleChange} placeholder="Event Type" />
                <input name="action" value={formData.action} onChange={handleChange} placeholder="Action" />
                <input name="protocol" value={formData.protocol} onChange={handleChange} placeholder="Protocol" />
                <input name="bytes_sent" type="number" value={formData.bytes_sent} onChange={handleChange} placeholder="Bytes Sent" />
                <input name="bytes_received" type="number" value={formData.bytes_received} onChange={handleChange} placeholder="Bytes Received" />
                <input name="duration" type="number" value={formData.duration} onChange={handleChange} placeholder="Duration" />
            </div>
            <button type="submit" style={{ marginTop: '10px', padding: '8px 16px', cursor: 'pointer' }}>
                Submit Event
            </button>
        </form>
    );
};

export default DetectionForm;