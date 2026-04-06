#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
from core.visa_manager import SpatioTemporalVisaManager
from core.spatial_ledger import SpatialLedger
from core.lord_brain import LordGovernanceBrain
from core.robot_navigation_pipeline import S2RobotNavigationPipeline

class S2EmbodiedSpatialBrain:
    def __init__(self):
        self.visa_mgr = SpatioTemporalVisaManager()
        self.ledger = SpatialLedger()
        self.lord = LordGovernanceBrain(self.visa_mgr, self.ledger)

    def process_tool_call(self, args: dict) -> str:
        try:
            action = args.get("action")
            if action == "REQUEST_VISA":
                res = self.visa_mgr.issue_visa(args.get("robot_id"), args.get("task"), args.get("requested_grids", []))
            elif action == "NAVIGATE_STEP":
                pipeline = S2RobotNavigationPipeline(args.get("robot_id"), args.get("visa_token"), self.lord)
                
                # 严格解析运动学与传感器载荷
                sensors = args.get("sensors", {})
                kinematics = args.get("kinematics", {"mass_kg": 20.0, "velocity_m_s": 0.0})
                peer_state = args.get("peer_state")
                
                res = pipeline.execute_step(args.get("target_hex"), sensors, kinematics, peer_state)
            else:
                res = {"status": "error", "message": "Unknown action. Use REQUEST_VISA or NAVIGATE_STEP."}
            return json.dumps({"status": "success", "data": res}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    brain = S2EmbodiedSpatialBrain()
    if len(sys.argv) > 1:
        print(brain.process_tool_call(json.loads(sys.argv[1])))
    else:
        print(json.dumps({"status": "ready", "message": "S2 Embodied Spatial Brain Online"}))