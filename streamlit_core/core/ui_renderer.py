#!/usr/bin/env python3
"""
UI Renderer for Streamlit Core
===============================

Handles all user interface rendering for the AIOS Streamlit UI system.
Renders sidebar, main interface, and all sub-components.

Key Features:
- Sidebar with system controls and state management
- Main interface with tabbed layout
- Chat interface for Luna
- Learning interface with meditation controls
- Analytics dashboard
- Settings configuration

Author: AIOS Development Team
Version: 1.0.0
"""

import streamlit as st

# Import from core modules
from .state_manager import StateManager
from .meditation_engine import MeditationEngine


class UIRenderer:
    """
    Renders the user interface for the AIOS Streamlit system.
    Coordinates between StateManager and MeditationEngine for UI updates.
    """
    
    def __init__(self, state_manager: StateManager, meditation_engine: MeditationEngine):
        """
        Initialize the UI renderer.
        
        Args:
            state_manager: StateManager instance for state operations
            meditation_engine: MeditationEngine instance for meditation features
        """
        self.state_manager = state_manager
        self.meditation_engine = meditation_engine
        
        print("🎨 UI Renderer Initialized")
    
    def render_sidebar(self):
        """Render the sidebar with persistent state management."""
        st.sidebar.title("🔧 System Controls")
        
        # Persistent State Management
        st.sidebar.subheader("💾 Persistent State")
        
        if st.sidebar.button("🗑️ Clear All State", type="secondary"):
            self.state_manager.clear_persistent_state()
            st.sidebar.success("State cleared!")
            st.rerun()
        
        # State Information
        state_info = self.state_manager.get_state_info()
        st.sidebar.write(f"**State Keys:** {state_info['num_keys']}")
        
        if state_info['num_keys'] > 0:
            st.sidebar.write(f"**State Size:** {state_info['size_kb']:.1f} KB")
        
        # Meditation Session Info
        session_info = self.meditation_engine.get_meditation_session_info()
        if session_info['active']:
            st.sidebar.subheader("🧘 Meditation Session")
            st.sidebar.write(f"**Status:** Active")
            st.sidebar.write(f"**Meditations:** {session_info['total_meditations']}")
            st.sidebar.write(f"**Karma:** {session_info['karma_gained']:.1f}")
        else:
            st.sidebar.subheader("🧘 Meditation Session")
            st.sidebar.write("**Status:** Inactive")
    
    def render_main_interface(self):
        """Render the main interface."""
        st.title("🌙 AIOS Clean - Luna Learning System")
        
        # Create tabs
        tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat", "🧠 Learning", "📊 Analytics", "🔧 Settings"])
        
        with tab1:
            self._render_chat_interface()
        
        with tab2:
            self._render_learning_interface()
        
        with tab3:
            self._render_analytics_interface()
        
        with tab4:
            self._render_settings_interface()
    
    def _render_chat_interface(self):
        """Render the chat interface."""
        st.header("💬 Chat with Luna")
        
        # Initialize chat history
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask Luna anything..."):
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate response (placeholder)
            with st.chat_message("assistant"):
                response = "Hello! I'm Luna, your AI learning companion. How can I help you today?"
                st.markdown(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    def _render_learning_interface(self):
        """Render the learning interface."""
        st.header("🧠 Luna Learning System")
        
        # Meditation Engine
        st.subheader("🧘 Meditation Engine")
        
        meditation_confirm = self.state_manager.get_state('meditation_confirm', False)
        
        if not meditation_confirm:
            st.info("Click below to start Luna's autonomous self-reflection mode")
            
            if st.button("🌙 Enter Meditation Mode (Self-Query Loop)", type="primary"):
                self.state_manager.set_state('meditation_confirm', True)
                st.rerun()
        else:
            st.warning("⚠️ Meditation mode requires confirmation")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ YES, Start Autonomous Reflection", type="primary"):
                    # Start meditation process
                    self.meditation_engine.start_meditation_session()
                    st.success("🧘 Meditation mode started!")
                    self.meditation_engine.update_heartbeat()
                    self.state_manager.set_state('meditation_confirm', False)
            
            with col2:
                if st.button("❌ Cancel", type="secondary"):
                    self.state_manager.set_state('meditation_confirm', False)
                    st.rerun()
        
        # Meditation Dashboard
        session_info = self.meditation_engine.get_meditation_session_info()
        if session_info['active']:
            st.subheader("📊 Meditation Dashboard")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Session Duration", f"{session_info['total_meditations']} cycles")
            with col2:
                st.metric("Karma Gained", f"{session_info['karma_gained']:.1f}")
            with col3:
                st.metric("Current State", session_info['current_state'])
            
            # Stop button
            if st.button("🛑 Stop Meditation", type="secondary"):
                self.meditation_engine.stop_meditation_session()
                st.success("Meditation session stopped")
                st.rerun()
    
    def _render_analytics_interface(self):
        """Render the analytics interface."""
        st.header("📊 System Analytics")
        
        # Placeholder for analytics
        st.info("Analytics interface coming soon...")
        st.write("This tab will display:")
        st.write("- System performance metrics")
        st.write("- Luna learning progress")
        st.write("- Meditation session history")
        st.write("- Karma accumulation trends")
    
    def _render_settings_interface(self):
        """Render the settings interface."""
        st.header("🔧 System Settings")
        
        # System configuration options
        st.subheader("System Configuration")
        
        # Model configuration display
        st.write("**Model Configuration:**")
        st.info("Model configuration is managed through config/model_config.json")
        
        # State management options
        st.subheader("State Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Persistent State:**")
            state_info = self.state_manager.get_state_info()
            st.write(f"- Keys: {state_info['num_keys']}")
            st.write(f"- Size: {state_info['size_kb']:.1f} KB")
            st.write(f"- File exists: {state_info['file_exists']}")
        
        with col2:
            st.write("**Meditation Engine:**")
            session_info = self.meditation_engine.get_meditation_session_info()
            st.write(f"- Active: {session_info['active']}")
            st.write(f"- Total sessions: {session_info['total_meditations']}")
            st.write(f"- Karma: {session_info['karma_gained']:.1f}")
        
        # Advanced settings
        st.subheader("Advanced Settings")
        st.info("Advanced settings interface coming soon...")

