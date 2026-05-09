# Table of Contents

* [resq\_mcp](#resq_mcp)
  * [annotations](#resq_mcp.annotations)
  * [Settings](#resq_mcp.Settings)
  * [settings](#resq_mcp.settings)
  * [Coordinates](#resq_mcp.Coordinates)
  * [DetectedObject](#resq_mcp.DetectedObject)
  * [DisasterScenario](#resq_mcp.DisasterScenario)
  * [ErrorResponse](#resq_mcp.ErrorResponse)
  * [Sector](#resq_mcp.Sector)
  * [DeploymentRequest](#resq_mcp.DeploymentRequest)
  * [DeploymentStatus](#resq_mcp.DeploymentStatus)
  * [NetworkStatus](#resq_mcp.NetworkStatus)
  * [SectorAnalysis](#resq_mcp.SectorAnalysis)
  * [SectorStatusSummary](#resq_mcp.SectorStatusSummary)
  * [SwarmStatus](#resq_mcp.SwarmStatus)
  * [get\_all\_sectors\_status](#resq_mcp.get_all_sectors_status)
  * [get\_drone\_swarm\_status](#resq_mcp.get_drone_swarm_status)
  * [request\_drone\_deployment](#resq_mcp.request_drone_deployment)
  * [scan\_current\_sector](#resq_mcp.scan_current_sector)
  * [OptimizationStrategy](#resq_mcp.OptimizationStrategy)
  * [SimulationRequest](#resq_mcp.SimulationRequest)
  * [get\_optimization\_strategy](#resq_mcp.get_optimization_strategy)
  * [run\_simulation](#resq_mcp.run_simulation)
  * [IncidentReport](#resq_mcp.IncidentReport)
  * [IncidentValidation](#resq_mcp.IncidentValidation)
  * [MissionParameters](#resq_mcp.MissionParameters)
  * [update\_mission\_params](#resq_mcp.update_mission_params)
  * [validate\_incident](#resq_mcp.validate_incident)
  * [PreAlert](#resq_mcp.PreAlert)
  * [VulnerabilityMap](#resq_mcp.VulnerabilityMap)
  * [get\_predictive\_alerts](#resq_mcp.get_predictive_alerts)
  * [get\_vulnerability\_map](#resq_mcp.get_vulnerability_map)
  * [mcp](#resq_mcp.mcp)
* [resq\_mcp.core](#resq_mcp.core)
  * [annotations](#resq_mcp.core.annotations)
  * [ConfigurationError](#resq_mcp.core.ConfigurationError)
  * [Settings](#resq_mcp.core.Settings)
  * [settings](#resq_mcp.core.settings)
  * [validate\_environment](#resq_mcp.core.validate_environment)
  * [MCPErrorFormatter](#resq_mcp.core.MCPErrorFormatter)
  * [Coordinates](#resq_mcp.core.Coordinates)
  * [DetectedObject](#resq_mcp.core.DetectedObject)
  * [DisasterScenario](#resq_mcp.core.DisasterScenario)
  * [ErrorResponse](#resq_mcp.core.ErrorResponse)
  * [Sector](#resq_mcp.core.Sector)
  * [verify\_api\_key](#resq_mcp.core.verify_api_key)
  * [setup\_telemetry](#resq_mcp.core.setup_telemetry)
  * [trace](#resq_mcp.core.trace)
  * [TimeoutConfig](#resq_mcp.core.TimeoutConfig)
  * [get\_default\_timeout](#resq_mcp.core.get_default_timeout)
  * [get\_max\_polling\_attempts](#resq_mcp.core.get_max_polling_attempts)
  * [get\_polling\_interval](#resq_mcp.core.get_polling_interval)
* [resq\_mcp.core.config](#resq_mcp.core.config)
  * [annotations](#resq_mcp.core.config.annotations)
  * [Literal](#resq_mcp.core.config.Literal)
  * [Field](#resq_mcp.core.config.Field)
  * [BaseSettings](#resq_mcp.core.config.BaseSettings)
  * [SettingsConfigDict](#resq_mcp.core.config.SettingsConfigDict)
  * [ConfigurationError](#resq_mcp.core.config.ConfigurationError)
  * [Settings](#resq_mcp.core.config.Settings)
    * [model\_config](#resq_mcp.core.config.Settings.model_config)
    * [PROJECT\_NAME](#resq_mcp.core.config.Settings.PROJECT_NAME)
    * [VERSION](#resq_mcp.core.config.Settings.VERSION)
    * [DEBUG](#resq_mcp.core.config.Settings.DEBUG)
    * [API\_KEY](#resq_mcp.core.config.Settings.API_KEY)
    * [PORT](#resq_mcp.core.config.Settings.PORT)
    * [HOST](#resq_mcp.core.config.Settings.HOST)
    * [SAFE\_MODE](#resq_mcp.core.config.Settings.SAFE_MODE)
    * [TELEMETRY\_BACKEND](#resq_mcp.core.config.Settings.TELEMETRY_BACKEND)
    * [OTEL\_EXPORTER\_OTLP\_ENDPOINT](#resq_mcp.core.config.Settings.OTEL_EXPORTER_OTLP_ENDPOINT)
    * [OTEL\_SERVICE\_NAME](#resq_mcp.core.config.Settings.OTEL_SERVICE_NAME)
  * [settings](#resq_mcp.core.config.settings)
  * [validate\_environment](#resq_mcp.core.config.validate_environment)
* [resq\_mcp.core.errors](#resq_mcp.core.errors)
  * [annotations](#resq_mcp.core.errors.annotations)
  * [json](#resq_mcp.core.errors.json)
  * [Any](#resq_mcp.core.errors.Any)
  * [MCPErrorFormatter](#resq_mcp.core.errors.MCPErrorFormatter)
    * [format\_error](#resq_mcp.core.errors.MCPErrorFormatter.format_error)
    * [from\_exception](#resq_mcp.core.errors.MCPErrorFormatter.from_exception)
* [resq\_mcp.core.models](#resq_mcp.core.models)
  * [annotations](#resq_mcp.core.models.annotations)
  * [UTC](#resq_mcp.core.models.UTC)
  * [datetime](#resq_mcp.core.models.datetime)
  * [Literal](#resq_mcp.core.models.Literal)
  * [BaseModel](#resq_mcp.core.models.BaseModel)
  * [Coordinates](#resq_mcp.core.models.Coordinates)
    * [lat](#resq_mcp.core.models.Coordinates.lat)
    * [lng](#resq_mcp.core.models.Coordinates.lng)
    * [status](#resq_mcp.core.models.Coordinates.status)
  * [Sector](#resq_mcp.core.models.Sector)
    * [id](#resq_mcp.core.models.Sector.id)
    * [coordinates](#resq_mcp.core.models.Sector.coordinates)
  * [DetectedObject](#resq_mcp.core.models.DetectedObject)
    * [name](#resq_mcp.core.models.DetectedObject.name)
    * [type](#resq_mcp.core.models.DetectedObject.type)
    * [confidence](#resq_mcp.core.models.DetectedObject.confidence)
    * [description](#resq_mcp.core.models.DetectedObject.description)
  * [DisasterScenario](#resq_mcp.core.models.DisasterScenario)
    * [type](#resq_mcp.core.models.DisasterScenario.type)
    * [name](#resq_mcp.core.models.DisasterScenario.name)
    * [confidence](#resq_mcp.core.models.DisasterScenario.confidence)
    * [description](#resq_mcp.core.models.DisasterScenario.description)
  * [ErrorResponse](#resq_mcp.core.models.ErrorResponse)
    * [status](#resq_mcp.core.models.ErrorResponse.status)
    * [message](#resq_mcp.core.models.ErrorResponse.message)
* [resq\_mcp.core.security](#resq_mcp.core.security)
  * [annotations](#resq_mcp.core.security.annotations)
  * [logging](#resq_mcp.core.security.logging)
  * [secrets](#resq_mcp.core.security.secrets)
  * [HTTPException](#resq_mcp.core.security.HTTPException)
  * [Request](#resq_mcp.core.security.Request)
  * [status](#resq_mcp.core.security.status)
  * [HTTPBearer](#resq_mcp.core.security.HTTPBearer)
  * [settings](#resq_mcp.core.security.settings)
  * [logger](#resq_mcp.core.security.logger)
  * [security\_scheme](#resq_mcp.core.security.security_scheme)
  * [verify\_api\_key](#resq_mcp.core.security.verify_api_key)
* [resq\_mcp.core.telemetry](#resq_mcp.core.telemetry)
  * [annotations](#resq_mcp.core.telemetry.annotations)
  * [functools](#resq_mcp.core.telemetry.functools)
  * [logging](#resq_mcp.core.telemetry.logging)
  * [re](#resq_mcp.core.telemetry.re)
  * [time](#resq_mcp.core.telemetry.time)
  * [contextmanager](#resq_mcp.core.telemetry.contextmanager)
  * [TYPE\_CHECKING](#resq_mcp.core.telemetry.TYPE_CHECKING)
  * [Any](#resq_mcp.core.telemetry.Any)
  * [ParamSpec](#resq_mcp.core.telemetry.ParamSpec)
  * [TypeVar](#resq_mcp.core.telemetry.TypeVar)
  * [settings](#resq_mcp.core.telemetry.settings)
  * [P](#resq_mcp.core.telemetry.P)
  * [R](#resq_mcp.core.telemetry.R)
  * [logger](#resq_mcp.core.telemetry.logger)
  * [tracer](#resq_mcp.core.telemetry.tracer)
  * [meter](#resq_mcp.core.telemetry.meter)
  * [setup\_telemetry](#resq_mcp.core.telemetry.setup_telemetry)
  * [metrics](#resq_mcp.core.telemetry.metrics)
  * [trace](#resq_mcp.core.telemetry.trace)
  * [span](#resq_mcp.core.telemetry.span)
  * [log\_event](#resq_mcp.core.telemetry.log_event)
  * [shutdown\_telemetry](#resq_mcp.core.telemetry.shutdown_telemetry)
* [resq\_mcp.core.timeout](#resq_mcp.core.timeout)
  * [annotations](#resq_mcp.core.timeout.annotations)
  * [os](#resq_mcp.core.timeout.os)
  * [dataclass](#resq_mcp.core.timeout.dataclass)
  * [TimeoutConfig](#resq_mcp.core.timeout.TimeoutConfig)
    * [total](#resq_mcp.core.timeout.TimeoutConfig.total)
    * [connect](#resq_mcp.core.timeout.TimeoutConfig.connect)
    * [read](#resq_mcp.core.timeout.TimeoutConfig.read)
  * [get\_default\_timeout](#resq_mcp.core.timeout.get_default_timeout)
  * [get\_max\_polling\_attempts](#resq_mcp.core.timeout.get_max_polling_attempts)
  * [get\_polling\_interval](#resq_mcp.core.timeout.get_polling_interval)
* [resq\_mcp.drone](#resq_mcp.drone)
  * [annotations](#resq_mcp.drone.annotations)
  * [DeploymentRequest](#resq_mcp.drone.DeploymentRequest)
  * [DeploymentStatus](#resq_mcp.drone.DeploymentStatus)
  * [NetworkStatus](#resq_mcp.drone.NetworkStatus)
  * [SectorAnalysis](#resq_mcp.drone.SectorAnalysis)
  * [SectorStatusSummary](#resq_mcp.drone.SectorStatusSummary)
  * [SwarmStatus](#resq_mcp.drone.SwarmStatus)
  * [get\_all\_sectors\_status](#resq_mcp.drone.get_all_sectors_status)
  * [get\_drone\_swarm\_status](#resq_mcp.drone.get_drone_swarm_status)
  * [request\_drone\_deployment](#resq_mcp.drone.request_drone_deployment)
  * [scan\_current\_sector](#resq_mcp.drone.scan_current_sector)
* [resq\_mcp.drone.models](#resq_mcp.drone.models)
  * [annotations](#resq_mcp.drone.models.annotations)
  * [datetime](#resq_mcp.drone.models.datetime)
  * [Literal](#resq_mcp.drone.models.Literal)
  * [BaseModel](#resq_mcp.drone.models.BaseModel)
  * [Field](#resq_mcp.drone.models.Field)
  * [Coordinates](#resq_mcp.drone.models.Coordinates)
  * [SectorAnalysis](#resq_mcp.drone.models.SectorAnalysis)
    * [sector\_id](#resq_mcp.drone.models.SectorAnalysis.sector_id)
    * [timestamp](#resq_mcp.drone.models.SectorAnalysis.timestamp)
    * [status](#resq_mcp.drone.models.SectorAnalysis.status)
    * [detected\_object](#resq_mcp.drone.models.SectorAnalysis.detected_object)
    * [disaster\_type](#resq_mcp.drone.models.SectorAnalysis.disaster_type)
    * [confidence](#resq_mcp.drone.models.SectorAnalysis.confidence)
    * [description](#resq_mcp.drone.models.SectorAnalysis.description)
    * [coordinates](#resq_mcp.drone.models.SectorAnalysis.coordinates)
    * [video\_proof\_url](#resq_mcp.drone.models.SectorAnalysis.video_proof_url)
    * [recommended\_action](#resq_mcp.drone.models.SectorAnalysis.recommended_action)
  * [SectorStatusSummary](#resq_mcp.drone.models.SectorStatusSummary)
    * [status](#resq_mcp.drone.models.SectorStatusSummary.status)
    * [detected\_object](#resq_mcp.drone.models.SectorStatusSummary.detected_object)
    * [confidence](#resq_mcp.drone.models.SectorStatusSummary.confidence)
  * [NetworkStatus](#resq_mcp.drone.models.NetworkStatus)
    * [timestamp](#resq_mcp.drone.models.NetworkStatus.timestamp)
    * [total\_sectors](#resq_mcp.drone.models.NetworkStatus.total_sectors)
    * [sectors](#resq_mcp.drone.models.NetworkStatus.sectors)
    * [critical\_alerts](#resq_mcp.drone.models.NetworkStatus.critical_alerts)
  * [SwarmStatus](#resq_mcp.drone.models.SwarmStatus)
    * [timestamp](#resq_mcp.drone.models.SwarmStatus.timestamp)
    * [total\_drones](#resq_mcp.drone.models.SwarmStatus.total_drones)
    * [active\_drones](#resq_mcp.drone.models.SwarmStatus.active_drones)
    * [average\_battery](#resq_mcp.drone.models.SwarmStatus.average_battery)
    * [network\_status](#resq_mcp.drone.models.SwarmStatus.network_status)
    * [last\_sync](#resq_mcp.drone.models.SwarmStatus.last_sync)
  * [DeploymentRequest](#resq_mcp.drone.models.DeploymentRequest)
    * [sector\_id](#resq_mcp.drone.models.DeploymentRequest.sector_id)
    * [priority](#resq_mcp.drone.models.DeploymentRequest.priority)
  * [DeploymentStatus](#resq_mcp.drone.models.DeploymentStatus)
    * [status](#resq_mcp.drone.models.DeploymentStatus.status)
    * [sector\_id](#resq_mcp.drone.models.DeploymentStatus.sector_id)
    * [priority](#resq_mcp.drone.models.DeploymentStatus.priority)
    * [drone\_id](#resq_mcp.drone.models.DeploymentStatus.drone_id)
    * [eta\_seconds](#resq_mcp.drone.models.DeploymentStatus.eta_seconds)
    * [timestamp](#resq_mcp.drone.models.DeploymentStatus.timestamp)
* [resq\_mcp.drone.service](#resq_mcp.drone.service)
  * [annotations](#resq_mcp.drone.service.annotations)
  * [random](#resq_mcp.drone.service.random)
  * [UTC](#resq_mcp.drone.service.UTC)
  * [datetime](#resq_mcp.drone.service.datetime)
  * [Final](#resq_mcp.drone.service.Final)
  * [Coordinates](#resq_mcp.drone.service.Coordinates)
  * [DisasterScenario](#resq_mcp.drone.service.DisasterScenario)
  * [ErrorResponse](#resq_mcp.drone.service.ErrorResponse)
  * [DeploymentStatus](#resq_mcp.drone.service.DeploymentStatus)
  * [NetworkStatus](#resq_mcp.drone.service.NetworkStatus)
  * [SectorAnalysis](#resq_mcp.drone.service.SectorAnalysis)
  * [SectorStatusSummary](#resq_mcp.drone.service.SectorStatusSummary)
  * [SwarmStatus](#resq_mcp.drone.service.SwarmStatus)
  * [DRONE\_SECTORS](#resq_mcp.drone.service.DRONE_SECTORS)
  * [DISASTER\_SCENARIOS](#resq_mcp.drone.service.DISASTER_SCENARIOS)
  * [scan\_current\_sector](#resq_mcp.drone.service.scan_current_sector)
  * [get\_all\_sectors\_status](#resq_mcp.drone.service.get_all_sectors_status)
  * [get\_drone\_swarm\_status](#resq_mcp.drone.service.get_drone_swarm_status)
  * [request\_drone\_deployment](#resq_mcp.drone.service.request_drone_deployment)
* [resq\_mcp.dtsop](#resq_mcp.dtsop)
  * [annotations](#resq_mcp.dtsop.annotations)
  * [OptimizationStrategy](#resq_mcp.dtsop.OptimizationStrategy)
  * [SimulationRequest](#resq_mcp.dtsop.SimulationRequest)
  * [get\_optimization\_strategy](#resq_mcp.dtsop.get_optimization_strategy)
  * [run\_simulation](#resq_mcp.dtsop.run_simulation)
* [resq\_mcp.dtsop.models](#resq_mcp.dtsop.models)
  * [annotations](#resq_mcp.dtsop.models.annotations)
  * [Literal](#resq_mcp.dtsop.models.Literal)
  * [BaseModel](#resq_mcp.dtsop.models.BaseModel)
  * [SimulationRequest](#resq_mcp.dtsop.models.SimulationRequest)
    * [scenario\_id](#resq_mcp.dtsop.models.SimulationRequest.scenario_id)
    * [sector\_id](#resq_mcp.dtsop.models.SimulationRequest.sector_id)
    * [disaster\_type](#resq_mcp.dtsop.models.SimulationRequest.disaster_type)
    * [parameters](#resq_mcp.dtsop.models.SimulationRequest.parameters)
    * [priority](#resq_mcp.dtsop.models.SimulationRequest.priority)
  * [OptimizationStrategy](#resq_mcp.dtsop.models.OptimizationStrategy)
    * [strategy\_id](#resq_mcp.dtsop.models.OptimizationStrategy.strategy_id)
    * [related\_alert\_id](#resq_mcp.dtsop.models.OptimizationStrategy.related_alert_id)
    * [recommended\_deployment](#resq_mcp.dtsop.models.OptimizationStrategy.recommended_deployment)
    * [evacuation\_routes](#resq_mcp.dtsop.models.OptimizationStrategy.evacuation_routes)
    * [estimated\_success\_rate](#resq_mcp.dtsop.models.OptimizationStrategy.estimated_success_rate)
    * [simulation\_proof\_url](#resq_mcp.dtsop.models.OptimizationStrategy.simulation_proof_url)
* [resq\_mcp.dtsop.service](#resq_mcp.dtsop.service)
  * [annotations](#resq_mcp.dtsop.service.annotations)
  * [random](#resq_mcp.dtsop.service.random)
  * [uuid](#resq_mcp.dtsop.service.uuid)
  * [Final](#resq_mcp.dtsop.service.Final)
  * [OptimizationStrategy](#resq_mcp.dtsop.service.OptimizationStrategy)
  * [SimulationRequest](#resq_mcp.dtsop.service.SimulationRequest)
  * [run\_simulation](#resq_mcp.dtsop.service.run_simulation)
  * [get\_optimization\_strategy](#resq_mcp.dtsop.service.get_optimization_strategy)
* [resq\_mcp.dtsop.tools](#resq_mcp.dtsop.tools)
  * [logging](#resq_mcp.dtsop.tools.logging)
  * [UTC](#resq_mcp.dtsop.tools.UTC)
  * [datetime](#resq_mcp.dtsop.tools.datetime)
  * [Context](#resq_mcp.dtsop.tools.Context)
  * [FastMCPError](#resq_mcp.dtsop.tools.FastMCPError)
  * [OptimizationStrategy](#resq_mcp.dtsop.tools.OptimizationStrategy)
  * [SimulationRequest](#resq_mcp.dtsop.tools.SimulationRequest)
  * [get\_optimization\_strategy](#resq_mcp.dtsop.tools.get_optimization_strategy)
  * [trigger\_sim](#resq_mcp.dtsop.tools.trigger_sim)
  * [MAX\_SIMULATIONS](#resq_mcp.dtsop.tools.MAX_SIMULATIONS)
  * [incidents](#resq_mcp.dtsop.tools.incidents)
  * [mcp](#resq_mcp.dtsop.tools.mcp)
  * [simulations](#resq_mcp.dtsop.tools.simulations)
  * [logger](#resq_mcp.dtsop.tools.logger)
  * [run\_simulation](#resq_mcp.dtsop.tools.run_simulation)
  * [get\_deployment\_strategy](#resq_mcp.dtsop.tools.get_deployment_strategy)
* [resq\_mcp.hce](#resq_mcp.hce)
  * [annotations](#resq_mcp.hce.annotations)
  * [IncidentReport](#resq_mcp.hce.IncidentReport)
  * [IncidentValidation](#resq_mcp.hce.IncidentValidation)
  * [MissionParameters](#resq_mcp.hce.MissionParameters)
  * [update\_mission\_params](#resq_mcp.hce.update_mission_params)
  * [validate\_incident](#resq_mcp.hce.validate_incident)
* [resq\_mcp.hce.models](#resq_mcp.hce.models)
  * [annotations](#resq_mcp.hce.models.annotations)
  * [datetime](#resq_mcp.hce.models.datetime)
  * [Literal](#resq_mcp.hce.models.Literal)
  * [BaseModel](#resq_mcp.hce.models.BaseModel)
  * [Field](#resq_mcp.hce.models.Field)
  * [IncidentReport](#resq_mcp.hce.models.IncidentReport)
    * [incident\_id](#resq_mcp.hce.models.IncidentReport.incident_id)
    * [source](#resq_mcp.hce.models.IncidentReport.source)
    * [sector\_id](#resq_mcp.hce.models.IncidentReport.sector_id)
    * [detected\_type](#resq_mcp.hce.models.IncidentReport.detected_type)
    * [confidence](#resq_mcp.hce.models.IncidentReport.confidence)
    * [evidence\_url](#resq_mcp.hce.models.IncidentReport.evidence_url)
    * [timestamp](#resq_mcp.hce.models.IncidentReport.timestamp)
  * [IncidentValidation](#resq_mcp.hce.models.IncidentValidation)
    * [incident\_id](#resq_mcp.hce.models.IncidentValidation.incident_id)
    * [is\_confirmed](#resq_mcp.hce.models.IncidentValidation.is_confirmed)
    * [validation\_source](#resq_mcp.hce.models.IncidentValidation.validation_source)
    * [correlated\_pre\_alert\_id](#resq_mcp.hce.models.IncidentValidation.correlated_pre_alert_id)
    * [notes](#resq_mcp.hce.models.IncidentValidation.notes)
  * [MissionParameters](#resq_mcp.hce.models.MissionParameters)
    * [mission\_id](#resq_mcp.hce.models.MissionParameters.mission_id)
    * [target\_sector](#resq_mcp.hce.models.MissionParameters.target_sector)
    * [authorized\_actions](#resq_mcp.hce.models.MissionParameters.authorized_actions)
    * [risk\_tolerance](#resq_mcp.hce.models.MissionParameters.risk_tolerance)
    * [strategy\_hash](#resq_mcp.hce.models.MissionParameters.strategy_hash)
    * [timestamp](#resq_mcp.hce.models.MissionParameters.timestamp)
* [resq\_mcp.hce.service](#resq_mcp.hce.service)
  * [annotations](#resq_mcp.hce.service.annotations)
  * [hashlib](#resq_mcp.hce.service.hashlib)
  * [uuid](#resq_mcp.hce.service.uuid)
  * [TYPE\_CHECKING](#resq_mcp.hce.service.TYPE_CHECKING)
  * [Final](#resq_mcp.hce.service.Final)
  * [IncidentReport](#resq_mcp.hce.service.IncidentReport)
  * [IncidentValidation](#resq_mcp.hce.service.IncidentValidation)
  * [MissionParameters](#resq_mcp.hce.service.MissionParameters)
  * [validate\_incident](#resq_mcp.hce.service.validate_incident)
  * [update\_mission\_params](#resq_mcp.hce.service.update_mission_params)
* [resq\_mcp.hce.tools](#resq_mcp.hce.tools)
  * [logging](#resq_mcp.hce.tools.logging)
  * [time](#resq_mcp.hce.tools.time)
  * [UTC](#resq_mcp.hce.tools.UTC)
  * [datetime](#resq_mcp.hce.tools.datetime)
  * [FastMCPError](#resq_mcp.hce.tools.FastMCPError)
  * [IncidentValidation](#resq_mcp.hce.tools.IncidentValidation)
  * [MissionParameters](#resq_mcp.hce.tools.MissionParameters)
  * [MAX\_INCIDENTS](#resq_mcp.hce.tools.MAX_INCIDENTS)
  * [MAX\_MISSIONS](#resq_mcp.hce.tools.MAX_MISSIONS)
  * [incidents](#resq_mcp.hce.tools.incidents)
  * [mcp](#resq_mcp.hce.tools.mcp)
  * [missions](#resq_mcp.hce.tools.missions)
  * [logger](#resq_mcp.hce.tools.logger)
  * [validate\_incident](#resq_mcp.hce.tools.validate_incident)
  * [update\_mission\_params](#resq_mcp.hce.tools.update_mission_params)
* [resq\_mcp.models](#resq_mcp.models)
  * [annotations](#resq_mcp.models.annotations)
  * [UTC](#resq_mcp.models.UTC)
  * [datetime](#resq_mcp.models.datetime)
  * [Literal](#resq_mcp.models.Literal)
  * [BaseModel](#resq_mcp.models.BaseModel)
  * [Field](#resq_mcp.models.Field)
  * [Coordinates](#resq_mcp.models.Coordinates)
    * [lat](#resq_mcp.models.Coordinates.lat)
    * [lng](#resq_mcp.models.Coordinates.lng)
    * [status](#resq_mcp.models.Coordinates.status)
  * [Sector](#resq_mcp.models.Sector)
    * [id](#resq_mcp.models.Sector.id)
    * [coordinates](#resq_mcp.models.Sector.coordinates)
  * [DetectedObject](#resq_mcp.models.DetectedObject)
    * [name](#resq_mcp.models.DetectedObject.name)
    * [type](#resq_mcp.models.DetectedObject.type)
    * [confidence](#resq_mcp.models.DetectedObject.confidence)
    * [description](#resq_mcp.models.DetectedObject.description)
  * [DisasterScenario](#resq_mcp.models.DisasterScenario)
    * [type](#resq_mcp.models.DisasterScenario.type)
    * [name](#resq_mcp.models.DisasterScenario.name)
    * [confidence](#resq_mcp.models.DisasterScenario.confidence)
    * [description](#resq_mcp.models.DisasterScenario.description)
  * [SectorAnalysis](#resq_mcp.models.SectorAnalysis)
    * [sector\_id](#resq_mcp.models.SectorAnalysis.sector_id)
    * [timestamp](#resq_mcp.models.SectorAnalysis.timestamp)
    * [status](#resq_mcp.models.SectorAnalysis.status)
    * [detected\_object](#resq_mcp.models.SectorAnalysis.detected_object)
    * [disaster\_type](#resq_mcp.models.SectorAnalysis.disaster_type)
    * [confidence](#resq_mcp.models.SectorAnalysis.confidence)
    * [description](#resq_mcp.models.SectorAnalysis.description)
    * [coordinates](#resq_mcp.models.SectorAnalysis.coordinates)
    * [video\_proof\_url](#resq_mcp.models.SectorAnalysis.video_proof_url)
    * [recommended\_action](#resq_mcp.models.SectorAnalysis.recommended_action)
  * [SectorStatusSummary](#resq_mcp.models.SectorStatusSummary)
    * [status](#resq_mcp.models.SectorStatusSummary.status)
    * [detected\_object](#resq_mcp.models.SectorStatusSummary.detected_object)
    * [confidence](#resq_mcp.models.SectorStatusSummary.confidence)
  * [NetworkStatus](#resq_mcp.models.NetworkStatus)
    * [timestamp](#resq_mcp.models.NetworkStatus.timestamp)
    * [total\_sectors](#resq_mcp.models.NetworkStatus.total_sectors)
    * [sectors](#resq_mcp.models.NetworkStatus.sectors)
    * [critical\_alerts](#resq_mcp.models.NetworkStatus.critical_alerts)
  * [SwarmStatus](#resq_mcp.models.SwarmStatus)
    * [timestamp](#resq_mcp.models.SwarmStatus.timestamp)
    * [total\_drones](#resq_mcp.models.SwarmStatus.total_drones)
    * [active\_drones](#resq_mcp.models.SwarmStatus.active_drones)
    * [average\_battery](#resq_mcp.models.SwarmStatus.average_battery)
    * [network\_status](#resq_mcp.models.SwarmStatus.network_status)
    * [last\_sync](#resq_mcp.models.SwarmStatus.last_sync)
  * [DeploymentRequest](#resq_mcp.models.DeploymentRequest)
    * [sector\_id](#resq_mcp.models.DeploymentRequest.sector_id)
    * [priority](#resq_mcp.models.DeploymentRequest.priority)
  * [DeploymentStatus](#resq_mcp.models.DeploymentStatus)
    * [status](#resq_mcp.models.DeploymentStatus.status)
    * [sector\_id](#resq_mcp.models.DeploymentStatus.sector_id)
    * [priority](#resq_mcp.models.DeploymentStatus.priority)
    * [drone\_id](#resq_mcp.models.DeploymentStatus.drone_id)
    * [eta\_seconds](#resq_mcp.models.DeploymentStatus.eta_seconds)
    * [timestamp](#resq_mcp.models.DeploymentStatus.timestamp)
  * [VulnerabilityMap](#resq_mcp.models.VulnerabilityMap)
    * [sector\_id](#resq_mcp.models.VulnerabilityMap.sector_id)
    * [population\_density](#resq_mcp.models.VulnerabilityMap.population_density)
    * [critical\_infrastructure](#resq_mcp.models.VulnerabilityMap.critical_infrastructure)
    * [flood\_risk](#resq_mcp.models.VulnerabilityMap.flood_risk)
    * [fire\_risk](#resq_mcp.models.VulnerabilityMap.fire_risk)
    * [last\_updated](#resq_mcp.models.VulnerabilityMap.last_updated)
  * [PreAlert](#resq_mcp.models.PreAlert)
    * [alert\_id](#resq_mcp.models.PreAlert.alert_id)
    * [sector\_id](#resq_mcp.models.PreAlert.sector_id)
    * [predicted\_disaster\_type](#resq_mcp.models.PreAlert.predicted_disaster_type)
    * [probability](#resq_mcp.models.PreAlert.probability)
    * [forecast\_horizon\_hours](#resq_mcp.models.PreAlert.forecast_horizon_hours)
    * [vulnerability\_context](#resq_mcp.models.PreAlert.vulnerability_context)
    * [generated\_at](#resq_mcp.models.PreAlert.generated_at)
  * [SimulationRequest](#resq_mcp.models.SimulationRequest)
    * [scenario\_id](#resq_mcp.models.SimulationRequest.scenario_id)
    * [sector\_id](#resq_mcp.models.SimulationRequest.sector_id)
    * [disaster\_type](#resq_mcp.models.SimulationRequest.disaster_type)
    * [parameters](#resq_mcp.models.SimulationRequest.parameters)
    * [priority](#resq_mcp.models.SimulationRequest.priority)
  * [OptimizationStrategy](#resq_mcp.models.OptimizationStrategy)
    * [strategy\_id](#resq_mcp.models.OptimizationStrategy.strategy_id)
    * [related\_alert\_id](#resq_mcp.models.OptimizationStrategy.related_alert_id)
    * [recommended\_deployment](#resq_mcp.models.OptimizationStrategy.recommended_deployment)
    * [evacuation\_routes](#resq_mcp.models.OptimizationStrategy.evacuation_routes)
    * [estimated\_success\_rate](#resq_mcp.models.OptimizationStrategy.estimated_success_rate)
    * [simulation\_proof\_url](#resq_mcp.models.OptimizationStrategy.simulation_proof_url)
  * [IncidentReport](#resq_mcp.models.IncidentReport)
    * [incident\_id](#resq_mcp.models.IncidentReport.incident_id)
    * [source](#resq_mcp.models.IncidentReport.source)
    * [sector\_id](#resq_mcp.models.IncidentReport.sector_id)
    * [detected\_type](#resq_mcp.models.IncidentReport.detected_type)
    * [confidence](#resq_mcp.models.IncidentReport.confidence)
    * [evidence\_url](#resq_mcp.models.IncidentReport.evidence_url)
    * [timestamp](#resq_mcp.models.IncidentReport.timestamp)
  * [IncidentValidation](#resq_mcp.models.IncidentValidation)
    * [incident\_id](#resq_mcp.models.IncidentValidation.incident_id)
    * [is\_confirmed](#resq_mcp.models.IncidentValidation.is_confirmed)
    * [validation\_source](#resq_mcp.models.IncidentValidation.validation_source)
    * [correlated\_pre\_alert\_id](#resq_mcp.models.IncidentValidation.correlated_pre_alert_id)
    * [notes](#resq_mcp.models.IncidentValidation.notes)
  * [MissionParameters](#resq_mcp.models.MissionParameters)
    * [mission\_id](#resq_mcp.models.MissionParameters.mission_id)
    * [target\_sector](#resq_mcp.models.MissionParameters.target_sector)
    * [authorized\_actions](#resq_mcp.models.MissionParameters.authorized_actions)
    * [risk\_tolerance](#resq_mcp.models.MissionParameters.risk_tolerance)
    * [strategy\_hash](#resq_mcp.models.MissionParameters.strategy_hash)
    * [timestamp](#resq_mcp.models.MissionParameters.timestamp)
  * [ErrorResponse](#resq_mcp.models.ErrorResponse)
    * [status](#resq_mcp.models.ErrorResponse.status)
    * [message](#resq_mcp.models.ErrorResponse.message)
* [resq\_mcp.pdie](#resq_mcp.pdie)
  * [annotations](#resq_mcp.pdie.annotations)
  * [PreAlert](#resq_mcp.pdie.PreAlert)
  * [VulnerabilityMap](#resq_mcp.pdie.VulnerabilityMap)
  * [get\_predictive\_alerts](#resq_mcp.pdie.get_predictive_alerts)
  * [get\_vulnerability\_map](#resq_mcp.pdie.get_vulnerability_map)
* [resq\_mcp.pdie.models](#resq_mcp.pdie.models)
  * [annotations](#resq_mcp.pdie.models.annotations)
  * [datetime](#resq_mcp.pdie.models.datetime)
  * [Literal](#resq_mcp.pdie.models.Literal)
  * [BaseModel](#resq_mcp.pdie.models.BaseModel)
  * [Field](#resq_mcp.pdie.models.Field)
  * [VulnerabilityMap](#resq_mcp.pdie.models.VulnerabilityMap)
    * [sector\_id](#resq_mcp.pdie.models.VulnerabilityMap.sector_id)
    * [population\_density](#resq_mcp.pdie.models.VulnerabilityMap.population_density)
    * [critical\_infrastructure](#resq_mcp.pdie.models.VulnerabilityMap.critical_infrastructure)
    * [flood\_risk](#resq_mcp.pdie.models.VulnerabilityMap.flood_risk)
    * [fire\_risk](#resq_mcp.pdie.models.VulnerabilityMap.fire_risk)
    * [last\_updated](#resq_mcp.pdie.models.VulnerabilityMap.last_updated)
  * [PreAlert](#resq_mcp.pdie.models.PreAlert)
    * [alert\_id](#resq_mcp.pdie.models.PreAlert.alert_id)
    * [sector\_id](#resq_mcp.pdie.models.PreAlert.sector_id)
    * [predicted\_disaster\_type](#resq_mcp.pdie.models.PreAlert.predicted_disaster_type)
    * [probability](#resq_mcp.pdie.models.PreAlert.probability)
    * [forecast\_horizon\_hours](#resq_mcp.pdie.models.PreAlert.forecast_horizon_hours)
    * [vulnerability\_context](#resq_mcp.pdie.models.PreAlert.vulnerability_context)
    * [generated\_at](#resq_mcp.pdie.models.PreAlert.generated_at)
* [resq\_mcp.pdie.service](#resq_mcp.pdie.service)
  * [annotations](#resq_mcp.pdie.service.annotations)
  * [random](#resq_mcp.pdie.service.random)
  * [uuid](#resq_mcp.pdie.service.uuid)
  * [Final](#resq_mcp.pdie.service.Final)
  * [ErrorResponse](#resq_mcp.pdie.service.ErrorResponse)
  * [PreAlert](#resq_mcp.pdie.service.PreAlert)
  * [VulnerabilityMap](#resq_mcp.pdie.service.VulnerabilityMap)
  * [VULNERABILITY\_DB](#resq_mcp.pdie.service.VULNERABILITY_DB)
  * [get\_vulnerability\_map](#resq_mcp.pdie.service.get_vulnerability_map)
  * [get\_predictive\_alerts](#resq_mcp.pdie.service.get_predictive_alerts)
* [resq\_mcp.prompts](#resq_mcp.prompts)
  * [re](#resq_mcp.prompts.re)
  * [FastMCPError](#resq_mcp.prompts.FastMCPError)
  * [mcp](#resq_mcp.prompts.mcp)
  * [incident\_response\_plan](#resq_mcp.prompts.incident_response_plan)
* [resq\_mcp.resources](#resq_mcp.resources)
  * [FastMCPError](#resq_mcp.resources.FastMCPError)
  * [mcp](#resq_mcp.resources.mcp)
  * [simulations](#resq_mcp.resources.simulations)
  * [get\_simulation\_status](#resq_mcp.resources.get_simulation_status)
  * [list\_active\_drones](#resq_mcp.resources.list_active_drones)
* [resq\_mcp.server](#resq_mcp.server)
  * [asyncio](#resq_mcp.server.asyncio)
  * [contextlib](#resq_mcp.server.contextlib)
  * [logging](#resq_mcp.server.logging)
  * [time](#resq_mcp.server.time)
  * [asynccontextmanager](#resq_mcp.server.asynccontextmanager)
  * [TYPE\_CHECKING](#resq_mcp.server.TYPE_CHECKING)
  * [Any](#resq_mcp.server.Any)
  * [FastMCP](#resq_mcp.server.FastMCP)
  * [settings](#resq_mcp.server.settings)
  * [validate\_environment](#resq_mcp.server.validate_environment)
  * [setup\_telemetry](#resq_mcp.server.setup_telemetry)
  * [logger](#resq_mcp.server.logger)
  * [MAX\_SIMULATIONS](#resq_mcp.server.MAX_SIMULATIONS)
  * [MAX\_INCIDENTS](#resq_mcp.server.MAX_INCIDENTS)
  * [MAX\_MISSIONS](#resq_mcp.server.MAX_MISSIONS)
  * [COMPLETED\_TTL\_SECONDS](#resq_mcp.server.COMPLETED_TTL_SECONDS)
  * [FAILED\_TTL\_SECONDS](#resq_mcp.server.FAILED_TTL_SECONDS)
  * [INCIDENT\_TTL\_SECONDS](#resq_mcp.server.INCIDENT_TTL_SECONDS)
  * [CONFIRMED\_INCIDENT\_TTL\_SECONDS](#resq_mcp.server.CONFIRMED_INCIDENT_TTL_SECONDS)
  * [MISSION\_TTL\_SECONDS](#resq_mcp.server.MISSION_TTL_SECONDS)
  * [simulations](#resq_mcp.server.simulations)
  * [incidents](#resq_mcp.server.incidents)
  * [missions](#resq_mcp.server.missions)
  * [lifespan](#resq_mcp.server.lifespan)
  * [mcp](#resq_mcp.server.mcp)
  * [simulation\_processor](#resq_mcp.server.simulation_processor)
  * [tools](#resq_mcp.server.tools)
  * [tools](#resq_mcp.server.tools)
  * [prompts](#resq_mcp.server.prompts)
  * [resources](#resq_mcp.server.resources)
  * [main](#resq_mcp.server.main)
* [resq\_mcp.telemetry](#resq_mcp.telemetry)
  * [annotations](#resq_mcp.telemetry.annotations)
  * [logging](#resq_mcp.telemetry.logging)
  * [TYPE\_CHECKING](#resq_mcp.telemetry.TYPE_CHECKING)
  * [settings](#resq_mcp.telemetry.settings)
  * [logger](#resq_mcp.telemetry.logger)
  * [setup\_telemetry](#resq_mcp.telemetry.setup_telemetry)
  * [trace](#resq_mcp.telemetry.trace)
* [resq\_mcp.tools](#resq_mcp.tools)
  * [annotations](#resq_mcp.tools.annotations)
  * [random](#resq_mcp.tools.random)
  * [UTC](#resq_mcp.tools.UTC)
  * [datetime](#resq_mcp.tools.datetime)
  * [Final](#resq_mcp.tools.Final)
  * [Coordinates](#resq_mcp.tools.Coordinates)
  * [DeploymentStatus](#resq_mcp.tools.DeploymentStatus)
  * [DisasterScenario](#resq_mcp.tools.DisasterScenario)
  * [ErrorResponse](#resq_mcp.tools.ErrorResponse)
  * [NetworkStatus](#resq_mcp.tools.NetworkStatus)
  * [SectorAnalysis](#resq_mcp.tools.SectorAnalysis)
  * [SectorStatusSummary](#resq_mcp.tools.SectorStatusSummary)
  * [SwarmStatus](#resq_mcp.tools.SwarmStatus)
  * [DRONE\_SECTORS](#resq_mcp.tools.DRONE_SECTORS)
  * [DISASTER\_SCENARIOS](#resq_mcp.tools.DISASTER_SCENARIOS)
  * [scan\_current\_sector](#resq_mcp.tools.scan_current_sector)
  * [get\_all\_sectors\_status](#resq_mcp.tools.get_all_sectors_status)
  * [get\_drone\_swarm\_status](#resq_mcp.tools.get_drone_swarm_status)
  * [request\_drone\_deployment](#resq_mcp.tools.request_drone_deployment)

<a id="resq_mcp"></a>

# resq\_mcp

ResQ MCP - Model Context Protocol server for disaster response coordination.

This package provides:
- PDIE (Predictive Disaster Intelligence Engine)
- DTSOP (Digital Twin Simulation & Optimization Platform)
- HCE (Hybrid Coordination Engine)

**Example**:

  from resq_mcp import mcp
  mcp.run()

<a id="resq_mcp.annotations"></a>

## annotations

<a id="resq_mcp.Settings"></a>

## Settings

<a id="resq_mcp.settings"></a>

## settings

<a id="resq_mcp.Coordinates"></a>

## Coordinates

<a id="resq_mcp.DetectedObject"></a>

## DetectedObject

<a id="resq_mcp.DisasterScenario"></a>

## DisasterScenario

<a id="resq_mcp.ErrorResponse"></a>

## ErrorResponse

<a id="resq_mcp.Sector"></a>

## Sector

<a id="resq_mcp.DeploymentRequest"></a>

## DeploymentRequest

<a id="resq_mcp.DeploymentStatus"></a>

## DeploymentStatus

<a id="resq_mcp.NetworkStatus"></a>

## NetworkStatus

<a id="resq_mcp.SectorAnalysis"></a>

## SectorAnalysis

<a id="resq_mcp.SectorStatusSummary"></a>

## SectorStatusSummary

<a id="resq_mcp.SwarmStatus"></a>

## SwarmStatus

<a id="resq_mcp.get_all_sectors_status"></a>

## get\_all\_sectors\_status

<a id="resq_mcp.get_drone_swarm_status"></a>

## get\_drone\_swarm\_status

<a id="resq_mcp.request_drone_deployment"></a>

## request\_drone\_deployment

<a id="resq_mcp.scan_current_sector"></a>

## scan\_current\_sector

<a id="resq_mcp.OptimizationStrategy"></a>

## OptimizationStrategy

<a id="resq_mcp.SimulationRequest"></a>

## SimulationRequest

<a id="resq_mcp.get_optimization_strategy"></a>

## get\_optimization\_strategy

<a id="resq_mcp.run_simulation"></a>

## run\_simulation

<a id="resq_mcp.IncidentReport"></a>

## IncidentReport

<a id="resq_mcp.IncidentValidation"></a>

## IncidentValidation

<a id="resq_mcp.MissionParameters"></a>

## MissionParameters

<a id="resq_mcp.update_mission_params"></a>

## update\_mission\_params

<a id="resq_mcp.validate_incident"></a>

## validate\_incident

<a id="resq_mcp.PreAlert"></a>

## PreAlert

<a id="resq_mcp.VulnerabilityMap"></a>

## VulnerabilityMap

<a id="resq_mcp.get_predictive_alerts"></a>

## get\_predictive\_alerts

<a id="resq_mcp.get_vulnerability_map"></a>

## get\_vulnerability\_map

<a id="resq_mcp.mcp"></a>

## mcp

<a id="resq_mcp.core"></a>

# resq\_mcp.core

Core cross-cutting utilities for the ResQ MCP server.

<a id="resq_mcp.core.annotations"></a>

## annotations

<a id="resq_mcp.core.ConfigurationError"></a>

## ConfigurationError

<a id="resq_mcp.core.Settings"></a>

## Settings

<a id="resq_mcp.core.settings"></a>

## settings

<a id="resq_mcp.core.validate_environment"></a>

## validate\_environment

<a id="resq_mcp.core.MCPErrorFormatter"></a>

## MCPErrorFormatter

<a id="resq_mcp.core.Coordinates"></a>

## Coordinates

<a id="resq_mcp.core.DetectedObject"></a>

## DetectedObject

<a id="resq_mcp.core.DisasterScenario"></a>

## DisasterScenario

<a id="resq_mcp.core.ErrorResponse"></a>

## ErrorResponse

<a id="resq_mcp.core.Sector"></a>

## Sector

<a id="resq_mcp.core.verify_api_key"></a>

## verify\_api\_key

<a id="resq_mcp.core.setup_telemetry"></a>

## setup\_telemetry

<a id="resq_mcp.core.trace"></a>

## trace

<a id="resq_mcp.core.TimeoutConfig"></a>

## TimeoutConfig

<a id="resq_mcp.core.get_default_timeout"></a>

## get\_default\_timeout

<a id="resq_mcp.core.get_max_polling_attempts"></a>

## get\_max\_polling\_attempts

<a id="resq_mcp.core.get_polling_interval"></a>

## get\_polling\_interval

<a id="resq_mcp.core.config"></a>

# resq\_mcp.core.config

Configuration management for the ResQ MCP server.

Settings are loaded from environment variables with sensible defaults.
Use a .env file or export environment variables to override.

Environment variables:
    RESQ_PROJECT_NAME: Display name for the MCP server
    RESQ_VERSION: Version string for the server
    RESQ_DEBUG: Enable debug logging (true/false)
    RESQ_API_KEY: API key for authenticated endpoints
    RESQ_PORT: Port for SSE server
    RESQ_HOST: Host to bind to
    RESQ_SAFE_MODE: If True, side-effecting tools are disabled or mocked safely

<a id="resq_mcp.core.config.annotations"></a>

## annotations

<a id="resq_mcp.core.config.Literal"></a>

## Literal

<a id="resq_mcp.core.config.Field"></a>

## Field

<a id="resq_mcp.core.config.BaseSettings"></a>

## BaseSettings

<a id="resq_mcp.core.config.SettingsConfigDict"></a>

## SettingsConfigDict

<a id="resq_mcp.core.config.ConfigurationError"></a>

## ConfigurationError Objects

```python
class ConfigurationError(Exception)
```

Raised when required configuration is missing or invalid.

<a id="resq_mcp.core.config.Settings"></a>

## Settings Objects

```python
class Settings(BaseSettings)
```

Application configuration via environment variables.

<a id="resq_mcp.core.config.Settings.model_config"></a>

#### model\_config

<a id="resq_mcp.core.config.Settings.PROJECT_NAME"></a>

#### PROJECT\_NAME

<a id="resq_mcp.core.config.Settings.VERSION"></a>

#### VERSION

<a id="resq_mcp.core.config.Settings.DEBUG"></a>

#### DEBUG

<a id="resq_mcp.core.config.Settings.API_KEY"></a>

#### API\_KEY

<a id="resq_mcp.core.config.Settings.PORT"></a>

#### PORT

<a id="resq_mcp.core.config.Settings.HOST"></a>

#### HOST

<a id="resq_mcp.core.config.Settings.SAFE_MODE"></a>

#### SAFE\_MODE

<a id="resq_mcp.core.config.Settings.TELEMETRY_BACKEND"></a>

#### TELEMETRY\_BACKEND

<a id="resq_mcp.core.config.Settings.OTEL_EXPORTER_OTLP_ENDPOINT"></a>

#### OTEL\_EXPORTER\_OTLP\_ENDPOINT

<a id="resq_mcp.core.config.Settings.OTEL_SERVICE_NAME"></a>

#### OTEL\_SERVICE\_NAME

<a id="resq_mcp.core.config.settings"></a>

#### settings

<a id="resq_mcp.core.config.validate_environment"></a>

#### validate\_environment

```python
def validate_environment(require_api_key: bool = False) -> None
```

Validate required environment variables at startup.

This function performs fail-fast validation by raising ConfigurationError
if any required environment variables are missing.

**Arguments**:

- `require_api_key` - If True, API_KEY must be set and not be the default dev token.
  

**Raises**:

- `ConfigurationError` - If any required environment variable is missing or invalid.
  

**Example**:

  >>> from resq_mcp.core.config import validate_environment
  >>> validate_environment(require_api_key=True)

<a id="resq_mcp.core.errors"></a>

# resq\_mcp.core.errors

Structured error handling for ResQ MCP tools.

Provides consistent, AI-client-friendly error responses with actionable
context. Inspired by Archon MCP server error handling patterns.

<a id="resq_mcp.core.errors.annotations"></a>

## annotations

<a id="resq_mcp.core.errors.json"></a>

## json

<a id="resq_mcp.core.errors.Any"></a>

## Any

<a id="resq_mcp.core.errors.MCPErrorFormatter"></a>

## MCPErrorFormatter Objects

```python
class MCPErrorFormatter()
```

Formats errors consistently for MCP AI clients.

<a id="resq_mcp.core.errors.MCPErrorFormatter.format_error"></a>

#### MCPErrorFormatter.format\_error

```python
@staticmethod
def format_error(error_type: str,
                 message: str,
                 details: dict[str, Any] | None = None,
                 suggestion: str | None = None,
                 http_status: int | None = None) -> str
```

Format a structured error response as JSON.

<a id="resq_mcp.core.errors.MCPErrorFormatter.from_exception"></a>

#### MCPErrorFormatter.from\_exception

```python
@staticmethod
def from_exception(exception: Exception,
                   operation: str,
                   context: dict[str, Any] | None = None) -> str
```

Format error from a Python exception.

<a id="resq_mcp.core.models"></a>

# resq\_mcp.core.models

Shared domain models for the ResQ MCP server.

These Pydantic models define the core data contracts shared across all subsystems.

<a id="resq_mcp.core.models.annotations"></a>

## annotations

<a id="resq_mcp.core.models.UTC"></a>

## UTC

<a id="resq_mcp.core.models.datetime"></a>

## datetime

<a id="resq_mcp.core.models.Literal"></a>

## Literal

<a id="resq_mcp.core.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.core.models.Coordinates"></a>

## Coordinates Objects

```python
class Coordinates(BaseModel)
```

Geographic coordinates with status indicator.

Represents a geographic point in decimal degrees (WGS84 datum)
with an associated status flag for monitoring.

**Attributes**:

- `lat` - Latitude in decimal degrees (-90 to +90).
- `lng` - Longitude in decimal degrees (-180 to +180).
- `status` - Current status indicator (e.g., "clear", "critical").
  

**Example**:

  >>> coords = Coordinates(lat=37.3417, lng=-121.9751, status="clear")
  >>> print(f"Position: &#123;coords.lat&#125;, &#123;coords.lng&#125;")

<a id="resq_mcp.core.models.Coordinates.lat"></a>

#### lat

<a id="resq_mcp.core.models.Coordinates.lng"></a>

#### lng

<a id="resq_mcp.core.models.Coordinates.status"></a>

#### status

<a id="resq_mcp.core.models.Sector"></a>

## Sector Objects

```python
class Sector(BaseModel)
```

A monitored geographic sector in the drone surveillance network.

Sectors are predefined geographic zones monitored by the drone fleet
for disaster detection and response coordination.

**Attributes**:

- `id` - Unique sector identifier (e.g., "Sector-1").
- `coordinates` - Center point coordinates with status.

<a id="resq_mcp.core.models.Sector.id"></a>

#### id

<a id="resq_mcp.core.models.Sector.coordinates"></a>

#### coordinates

<a id="resq_mcp.core.models.DetectedObject"></a>

## DetectedObject Objects

```python
class DetectedObject(BaseModel)
```

An object detected by drone sensors during surveillance.

Represents the output of edge AI object detection running on drone
hardware or ground processing stations.

**Attributes**:

- `name` - Human-readable name of detected object (default: "None").
- `type` - Classification type (e.g., "fire", "vehicle", "person").
- `confidence` - Detection confidence score (0.0 to 1.0).
- `description` - Detailed description of the detection.

<a id="resq_mcp.core.models.DetectedObject.name"></a>

#### name

<a id="resq_mcp.core.models.DetectedObject.type"></a>

#### type

<a id="resq_mcp.core.models.DetectedObject.confidence"></a>

#### confidence

<a id="resq_mcp.core.models.DetectedObject.description"></a>

#### description

<a id="resq_mcp.core.models.DisasterScenario"></a>

## DisasterScenario Objects

```python
class DisasterScenario(BaseModel)
```

A disaster scenario template for simulation and detection.

Defines the characteristics of a disaster type that can be detected
by drone surveillance or used as input for digital twin simulations.

**Attributes**:

- `type` - Disaster category (e.g., "wildfire", "flood", "earthquake").
- `name` - Human-readable scenario name.
- `confidence` - Detection confidence or scenario likelihood (0.0 to 1.0).
- `description` - Detailed scenario description including characteristics.

<a id="resq_mcp.core.models.DisasterScenario.type"></a>

#### type

<a id="resq_mcp.core.models.DisasterScenario.name"></a>

#### name

<a id="resq_mcp.core.models.DisasterScenario.confidence"></a>

#### confidence

<a id="resq_mcp.core.models.DisasterScenario.description"></a>

#### description

<a id="resq_mcp.core.models.ErrorResponse"></a>

## ErrorResponse Objects

```python
class ErrorResponse(BaseModel)
```

Standard error response for failed operations.

Used across all subsystems to provide consistent error messaging.
Returned instead of raising exceptions for expected error conditions
(e.g., invalid sector ID, missing data).

**Attributes**:

- `status` - Always "error" to distinguish from success responses.
- `message` - Human-readable error description.
  

**Example**:

  >>> error = ErrorResponse(message="Sector not found")
  >>> if isinstance(result, ErrorResponse):
  ...     print(f"Error: &#123;result.message&#125;")

<a id="resq_mcp.core.models.ErrorResponse.status"></a>

#### status

<a id="resq_mcp.core.models.ErrorResponse.message"></a>

#### message

<a id="resq_mcp.core.security"></a>

# resq\_mcp.core.security

Security utilities for the ResQ MCP server.

Provides API key verification for authenticated endpoints using FastAPI's
HTTPBearer security scheme for token extraction.

**Notes**:

  This implementation uses a simple comparison against the configured API_KEY.
  Production deployments should use secure token storage and validation.

<a id="resq_mcp.core.security.annotations"></a>

## annotations

<a id="resq_mcp.core.security.logging"></a>

## logging

<a id="resq_mcp.core.security.secrets"></a>

## secrets

<a id="resq_mcp.core.security.HTTPException"></a>

## HTTPException

<a id="resq_mcp.core.security.Request"></a>

## Request

<a id="resq_mcp.core.security.status"></a>

## status

<a id="resq_mcp.core.security.HTTPBearer"></a>

## HTTPBearer

<a id="resq_mcp.core.security.settings"></a>

## settings

<a id="resq_mcp.core.security.logger"></a>

#### logger

<a id="resq_mcp.core.security.security_scheme"></a>

#### security\_scheme

<a id="resq_mcp.core.security.verify_api_key"></a>

#### verify\_api\_key

```python
def verify_api_key(request: Request) -> str
```

Verify the Bearer token against the configured API_KEY.

Used as a dependency for SSE endpoints if wrapping in FastAPI.
For FastMCP's SSE adapter, authentication may need to be handled
at the deployment level (Ingress/Gateway) for strict OAuth.

**Arguments**:

- `request` - The incoming FastAPI request.
  

**Returns**:

  The validated API token.
  

**Raises**:

- `HTTPException` - 401 if missing/invalid auth scheme, 403 if invalid key.

<a id="resq_mcp.core.telemetry"></a>

# resq\_mcp.core.telemetry

Telemetry subsystem for the ResQ MCP server.

Provides unified OpenTelemetry tracing, Prometheus-compatible metrics,
and structured logging with automatic PII redaction.

<a id="resq_mcp.core.telemetry.annotations"></a>

## annotations

<a id="resq_mcp.core.telemetry.functools"></a>

## functools

<a id="resq_mcp.core.telemetry.logging"></a>

## logging

<a id="resq_mcp.core.telemetry.re"></a>

## re

<a id="resq_mcp.core.telemetry.time"></a>

## time

<a id="resq_mcp.core.telemetry.contextmanager"></a>

## contextmanager

<a id="resq_mcp.core.telemetry.TYPE_CHECKING"></a>

## TYPE\_CHECKING

<a id="resq_mcp.core.telemetry.Any"></a>

## Any

<a id="resq_mcp.core.telemetry.ParamSpec"></a>

## ParamSpec

<a id="resq_mcp.core.telemetry.TypeVar"></a>

## TypeVar

<a id="resq_mcp.core.telemetry.settings"></a>

## settings

<a id="resq_mcp.core.telemetry.P"></a>

#### P

<a id="resq_mcp.core.telemetry.R"></a>

#### R

<a id="resq_mcp.core.telemetry.logger"></a>

#### logger

<a id="resq_mcp.core.telemetry.tracer"></a>

#### tracer

<a id="resq_mcp.core.telemetry.meter"></a>

#### meter

<a id="resq_mcp.core.telemetry.setup_telemetry"></a>

#### setup\_telemetry

```python
def setup_telemetry() -> None
```

Initialize OpenTelemetry tracing and metrics.

<a id="resq_mcp.core.telemetry.metrics"></a>

#### metrics

<a id="resq_mcp.core.telemetry.trace"></a>

#### trace

```python
def trace(_func_or_name: Callable[P, R] | str | None = None,
          name: str | None = None,
          *,
          record_args: bool = False,
          record_result: bool = False) -> Any
```

Instrument a function with an OpenTelemetry span.

<a id="resq_mcp.core.telemetry.span"></a>

#### span

```python
@contextmanager
def span(name: str,
         attributes: dict[str, Any] | None = None) -> Generator[Any]
```

<a id="resq_mcp.core.telemetry.log_event"></a>

#### log\_event

```python
def log_event(event: str, level: int = logging.INFO, **attrs: Any) -> None
```

<a id="resq_mcp.core.telemetry.shutdown_telemetry"></a>

#### shutdown\_telemetry

```python
def shutdown_telemetry(timeout_ms: int = 5_000) -> None
```

<a id="resq_mcp.core.timeout"></a>

# resq\_mcp.core.timeout

Centralized timeout configuration for ResQ MCP server.

Provides consistent, env-var-configurable timeout values across all tools.
Inspired by Archon MCP server timeout patterns.

Environment variables:
    RESQ_REQUEST_TIMEOUT: Total request timeout in seconds (default: 30)
    RESQ_CONNECT_TIMEOUT: Connection timeout in seconds (default: 5)
    RESQ_READ_TIMEOUT: Read timeout in seconds (default: 20)
    RESQ_POLLING_BASE_INTERVAL: Base polling interval in seconds (default: 1)
    RESQ_POLLING_MAX_INTERVAL: Max polling interval in seconds (default: 5)
    RESQ_MAX_POLLING_ATTEMPTS: Max polling attempts (default: 30)

<a id="resq_mcp.core.timeout.annotations"></a>

## annotations

<a id="resq_mcp.core.timeout.os"></a>

## os

<a id="resq_mcp.core.timeout.dataclass"></a>

## dataclass

<a id="resq_mcp.core.timeout.TimeoutConfig"></a>

## TimeoutConfig Objects

```python
@dataclass(frozen=True)
class TimeoutConfig()
```

Immutable timeout configuration.

<a id="resq_mcp.core.timeout.TimeoutConfig.total"></a>

#### total

<a id="resq_mcp.core.timeout.TimeoutConfig.connect"></a>

#### connect

<a id="resq_mcp.core.timeout.TimeoutConfig.read"></a>

#### read

<a id="resq_mcp.core.timeout.get_default_timeout"></a>

#### get\_default\_timeout

```python
def get_default_timeout() -> TimeoutConfig
```

Get default timeout configuration from environment or defaults.

<a id="resq_mcp.core.timeout.get_max_polling_attempts"></a>

#### get\_max\_polling\_attempts

```python
def get_max_polling_attempts() -> int
```

Get maximum number of polling attempts.

<a id="resq_mcp.core.timeout.get_polling_interval"></a>

#### get\_polling\_interval

```python
def get_polling_interval(attempt: int) -> float
```

Get polling interval with exponential backoff.

**Arguments**:

- `attempt` - Current attempt number (0-based).
  

**Returns**:

  Sleep interval in seconds.

<a id="resq_mcp.drone"></a>

# resq\_mcp.drone

Drone feed domain package.

<a id="resq_mcp.drone.annotations"></a>

## annotations

<a id="resq_mcp.drone.DeploymentRequest"></a>

## DeploymentRequest

<a id="resq_mcp.drone.DeploymentStatus"></a>

## DeploymentStatus

<a id="resq_mcp.drone.NetworkStatus"></a>

## NetworkStatus

<a id="resq_mcp.drone.SectorAnalysis"></a>

## SectorAnalysis

<a id="resq_mcp.drone.SectorStatusSummary"></a>

## SectorStatusSummary

<a id="resq_mcp.drone.SwarmStatus"></a>

## SwarmStatus

<a id="resq_mcp.drone.get_all_sectors_status"></a>

## get\_all\_sectors\_status

<a id="resq_mcp.drone.get_drone_swarm_status"></a>

## get\_drone\_swarm\_status

<a id="resq_mcp.drone.request_drone_deployment"></a>

## request\_drone\_deployment

<a id="resq_mcp.drone.scan_current_sector"></a>

## scan\_current\_sector

<a id="resq_mcp.drone.models"></a>

# resq\_mcp.drone.models

Drone feed domain models for the ResQ MCP server.

<a id="resq_mcp.drone.models.annotations"></a>

## annotations

<a id="resq_mcp.drone.models.datetime"></a>

## datetime

<a id="resq_mcp.drone.models.Literal"></a>

## Literal

<a id="resq_mcp.drone.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.drone.models.Field"></a>

## Field

<a id="resq_mcp.drone.models.Coordinates"></a>

## Coordinates

<a id="resq_mcp.drone.models.SectorAnalysis"></a>

## SectorAnalysis Objects

```python
class SectorAnalysis(BaseModel)
```

Complete analysis result from a sector surveillance scan.

Contains all detection data, evidence links, and recommended actions
from a drone sector scan. Used for incident reporting and blockchain
evidence submission.

**Attributes**:

- `sector_id` - Identifier of the scanned sector.
- `timestamp` - UTC timestamp of the analysis (auto-generated).
- `status` - Overall status (e.g., "clear", "CRITICAL_ALERT").
- `detected_object` - Primary object or hazard detected.
- `disaster_type` - Classified disaster type if applicable.
- `confidence` - Detection confidence score (0.0 to 1.0).
- `description` - Detailed analysis description.
- `coordinates` - Geographic coordinates of the detection.
- `video_proof_url` - NeoFS/IPFS URL for video evidence.
- `recommended_action` - Suggested next action (e.g., "IMMEDIATE_REPORT_TO_BLOCKCHAIN").

<a id="resq_mcp.drone.models.SectorAnalysis.sector_id"></a>

#### sector\_id

<a id="resq_mcp.drone.models.SectorAnalysis.timestamp"></a>

#### timestamp

<a id="resq_mcp.drone.models.SectorAnalysis.status"></a>

#### status

<a id="resq_mcp.drone.models.SectorAnalysis.detected_object"></a>

#### detected\_object

<a id="resq_mcp.drone.models.SectorAnalysis.disaster_type"></a>

#### disaster\_type

<a id="resq_mcp.drone.models.SectorAnalysis.confidence"></a>

#### confidence

<a id="resq_mcp.drone.models.SectorAnalysis.description"></a>

#### description

<a id="resq_mcp.drone.models.SectorAnalysis.coordinates"></a>

#### coordinates

<a id="resq_mcp.drone.models.SectorAnalysis.video_proof_url"></a>

#### video\_proof\_url

<a id="resq_mcp.drone.models.SectorAnalysis.recommended_action"></a>

#### recommended\_action

<a id="resq_mcp.drone.models.SectorStatusSummary"></a>

## SectorStatusSummary Objects

```python
class SectorStatusSummary(BaseModel)
```

Condensed status summary for network-wide sector monitoring.

Lightweight representation used in network status dashboards and
overview displays. Excludes detailed evidence and coordinates.

**Attributes**:

- `status` - Current sector status indicator.
- `detected_object` - Primary detected object or "None".
- `confidence` - Overall confidence score for the status.

<a id="resq_mcp.drone.models.SectorStatusSummary.status"></a>

#### status

<a id="resq_mcp.drone.models.SectorStatusSummary.detected_object"></a>

#### detected\_object

<a id="resq_mcp.drone.models.SectorStatusSummary.confidence"></a>

#### confidence

<a id="resq_mcp.drone.models.NetworkStatus"></a>

## NetworkStatus Objects

```python
class NetworkStatus(BaseModel)
```

Aggregate status of the entire drone surveillance network.

Provides a network-wide view of all monitored sectors and critical
alert counts for operator dashboards and system health monitoring.

**Attributes**:

- `timestamp` - UTC timestamp of the status snapshot (auto-generated).
- `total_sectors` - Total number of monitored sectors.
- `sectors` - Mapping of sector IDs to their status summaries.
- `critical_alerts` - Count of sectors with critical alerts active.

<a id="resq_mcp.drone.models.NetworkStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.drone.models.NetworkStatus.total_sectors"></a>

#### total\_sectors

<a id="resq_mcp.drone.models.NetworkStatus.sectors"></a>

#### sectors

<a id="resq_mcp.drone.models.NetworkStatus.critical_alerts"></a>

#### critical\_alerts

<a id="resq_mcp.drone.models.SwarmStatus"></a>

## SwarmStatus Objects

```python
class SwarmStatus(BaseModel)
```

Real-time operational status of the drone swarm.

Aggregates health metrics across all drones in the fleet including
battery levels, connectivity status, and deployment state.

**Attributes**:

- `timestamp` - UTC timestamp of the status snapshot (auto-generated).
- `total_drones` - Total number of drones in the fleet.
- `active_drones` - Number of drones currently deployed and operational.
- `average_battery` - Fleet-wide average battery percentage (0-100).
- `network_status` - Overall network health (e.g., "operational", "degraded").
- `last_sync` - UTC timestamp of last successful sync with ground station.

<a id="resq_mcp.drone.models.SwarmStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.drone.models.SwarmStatus.total_drones"></a>

#### total\_drones

<a id="resq_mcp.drone.models.SwarmStatus.active_drones"></a>

#### active\_drones

<a id="resq_mcp.drone.models.SwarmStatus.average_battery"></a>

#### average\_battery

<a id="resq_mcp.drone.models.SwarmStatus.network_status"></a>

#### network\_status

<a id="resq_mcp.drone.models.SwarmStatus.last_sync"></a>

#### last\_sync

<a id="resq_mcp.drone.models.DeploymentRequest"></a>

## DeploymentRequest Objects

```python
class DeploymentRequest(BaseModel)
```

Request for immediate drone deployment to a specific sector.

Used by operators or automated systems to request drone dispatch
to sectors requiring surveillance or emergency response.

**Attributes**:

- `sector_id` - Target sector identifier for deployment.
- `priority` - Deployment urgency level (low/medium/high/critical).
  Higher priority requests preempt lower priority missions.

<a id="resq_mcp.drone.models.DeploymentRequest.sector_id"></a>

#### sector\_id

<a id="resq_mcp.drone.models.DeploymentRequest.priority"></a>

#### priority

<a id="resq_mcp.drone.models.DeploymentStatus"></a>

## DeploymentStatus Objects

```python
class DeploymentStatus(BaseModel)
```

Response status for a drone deployment request.

Provides confirmation and tracking information for a deployment request
including assigned drone and estimated arrival time.

**Attributes**:

- `status` - Deployment state (e.g., "deployed", "en_route", "completed").
- `sector_id` - Target sector identifier.
- `priority` - Assigned priority level.
- `drone_id` - Identifier of the assigned drone unit.
- `eta_seconds` - Estimated time to arrival in seconds.
- `timestamp` - UTC timestamp of the status update (auto-generated).

<a id="resq_mcp.drone.models.DeploymentStatus.status"></a>

#### status

<a id="resq_mcp.drone.models.DeploymentStatus.sector_id"></a>

#### sector\_id

<a id="resq_mcp.drone.models.DeploymentStatus.priority"></a>

#### priority

<a id="resq_mcp.drone.models.DeploymentStatus.drone_id"></a>

#### drone\_id

<a id="resq_mcp.drone.models.DeploymentStatus.eta_seconds"></a>

#### eta\_seconds

<a id="resq_mcp.drone.models.DeploymentStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.drone.service"></a>

# resq\_mcp.drone.service

Drone feed tools for the ResQ MCP server.

This module provides simulated drone feed functionality for development and testing.
It generates pseudo-random telemetry and analysis data for drone network sectors.

The simulation includes:
- 4 monitored sectors with predefined coordinates
- Random disaster scenario detection (fire, flood, medical, debris)
- Swarm status with variable battery and connectivity
- Drone deployment request handling

<a id="resq_mcp.drone.service.annotations"></a>

## annotations

<a id="resq_mcp.drone.service.random"></a>

## random

<a id="resq_mcp.drone.service.UTC"></a>

## UTC

<a id="resq_mcp.drone.service.datetime"></a>

## datetime

<a id="resq_mcp.drone.service.Final"></a>

## Final

<a id="resq_mcp.drone.service.Coordinates"></a>

## Coordinates

<a id="resq_mcp.drone.service.DisasterScenario"></a>

## DisasterScenario

<a id="resq_mcp.drone.service.ErrorResponse"></a>

## ErrorResponse

<a id="resq_mcp.drone.service.DeploymentStatus"></a>

## DeploymentStatus

<a id="resq_mcp.drone.service.NetworkStatus"></a>

## NetworkStatus

<a id="resq_mcp.drone.service.SectorAnalysis"></a>

## SectorAnalysis

<a id="resq_mcp.drone.service.SectorStatusSummary"></a>

## SectorStatusSummary

<a id="resq_mcp.drone.service.SwarmStatus"></a>

## SwarmStatus

<a id="resq_mcp.drone.service.DRONE_SECTORS"></a>

#### DRONE\_SECTORS

<a id="resq_mcp.drone.service.DISASTER_SCENARIOS"></a>

#### DISASTER\_SCENARIOS

<a id="resq_mcp.drone.service.scan_current_sector"></a>

#### scan\_current\_sector

```python
def scan_current_sector(
        sector_id: str = "Sector-1") -> SectorAnalysis | ErrorResponse
```

Scan a specific sector for anomalies using simulated drone sensors.

Simulates drone-based surveillance with probabilistic disaster detection.
In production, this would integrate with actual drone telemetry and
edge AI processing results from the MCP drone feed server.

Detection Logic:
- 30% probability of detecting a disaster scenario per scan
- Randomly selects from predefined disaster templates
- Generates NeoFS evidence URL for blockchain submission
- Returns "clear" status if no anomalies detected

**Arguments**:

- `sector_id` - The sector to scan ("Sector-1" through "Sector-4").
  Default is "Sector-1".
  

**Returns**:

- `SectorAnalysis` - Complete scan results with detection data and
  recommended actions if sector exists.
- `ErrorResponse` - Error message if sector_id is invalid.
  

**Example**:

  >>> result = scan_current_sector("Sector-2")
  >>> if isinstance(result, SectorAnalysis):
  ...     if result.status == "CRITICAL_ALERT":
  ...         print(f"Alert: &#123;result.detected_object&#125;")
  ...         print(f"Action: &#123;result.recommended_action&#125;")
  

**Notes**:

  This is a simulation function. Production deployment would replace
  random detection with actual ML model inference on drone imagery.

<a id="resq_mcp.drone.service.get_all_sectors_status"></a>

#### get\_all\_sectors\_status

```python
def get_all_sectors_status() -> NetworkStatus
```

Get the status of all monitored sectors in the surveillance network.

Aggregates scan results across all configured sectors to provide
network-wide situational awareness for operator dashboards.

**Returns**:

- `NetworkStatus` - Complete network status including:
  - Total sector count
  - Per-sector status summaries (detected objects, confidence)
  - Critical alert count for priority filtering
  - Timestamp of status generation
  

**Example**:

  >>> status = get_all_sectors_status()
  >>> print(f"Network: &#123;status.total_sectors&#125; sectors")
  >>> print(f"Critical Alerts: &#123;status.critical_alerts&#125;")
  >>> for sector_id, summary in status.sectors.items():
  ...     if summary.status == "CRITICAL_ALERT":
  ...         print(f"&#123;sector_id&#125;: &#123;summary.detected_object&#125;")
  

**Notes**:

  Calls scan_current_sector() for each sector, so inherits its
  simulation behavior (random detection).

<a id="resq_mcp.drone.service.get_drone_swarm_status"></a>

#### get\_drone\_swarm\_status

```python
def get_drone_swarm_status() -> SwarmStatus
```

Get the overall operational status of the drone swarm.

Provides fleet-wide health metrics for monitoring drone readiness
and availability. Used by operators to assess deployment capacity.

Simulation Behavior:
- Total drones: Fixed at 3 for development
- Active drones: Random 2-3 (some may be charging/maintenance)
- Average battery: Random 60-100% (simulated degradation)
- Network status: Always "operational" in dev mode

**Returns**:

- `SwarmStatus` - Fleet metrics including:
  - Total and active drone counts
  - Fleet-wide average battery percentage
  - Network connectivity status
  - Last sync timestamp (auto-generated)
  

**Example**:

  >>> swarm = get_drone_swarm_status()
  >>> if swarm.average_battery < 30:
  ...     print("WARNING: Low fleet battery")
  >>> print(f"&#123;swarm.active_drones&#125;/&#123;swarm.total_drones&#125; drones active")
  

**Notes**:

  Production would aggregate real telemetry from the MCP drone feed
  server, reporting actual battery, GPS lock, and link quality.

<a id="resq_mcp.drone.service.request_drone_deployment"></a>

#### request\_drone\_deployment

```python
def request_drone_deployment(
        sector_id: str,
        priority: str = "high") -> DeploymentStatus | ErrorResponse
```

Request deployment of a drone to a specific sector.

Simulates drone dispatch request handling with immediate assignment.
In production, this would interface with the drone control module
and mission planning system to allocate resources.

Simulation Behavior:
- Assigns random drone unit (UNIT-001 through UNIT-003)
- Generates random ETA (30-120 seconds)
- Always returns "deployed" status if sector valid

**Arguments**:

- `sector_id` - The target sector for deployment (e.g., "Sector-1").
- `priority` - Deployment urgency level. Higher priority missions
  preempt lower priority tasks. Valid values:
  - "low": Routine surveillance
  - "medium": Follow-up investigation
  - "high" (default): Active incident response
  - "critical": Immediate life-threatening situation
  

**Returns**:

- `DeploymentStatus` - Confirmation with assigned drone and ETA if
  sector is valid.
- `ErrorResponse` - Error message if sector_id is invalid.
  

**Example**:

  >>> status = request_drone_deployment("Sector-3", priority="critical")
  >>> if isinstance(status, DeploymentStatus):
  ...     print(f"Drone &#123;status.drone_id&#125; dispatched")
  ...     print(f"ETA: &#123;status.eta_seconds&#125; seconds")
  

**Notes**:

  Production would check drone availability, battery levels, and
  weather conditions before confirming deployment.

<a id="resq_mcp.dtsop"></a>

# resq\_mcp.dtsop

DTSOP - Digital Twin Simulation & Optimization Platform package.

<a id="resq_mcp.dtsop.annotations"></a>

## annotations

<a id="resq_mcp.dtsop.OptimizationStrategy"></a>

## OptimizationStrategy

<a id="resq_mcp.dtsop.SimulationRequest"></a>

## SimulationRequest

<a id="resq_mcp.dtsop.get_optimization_strategy"></a>

## get\_optimization\_strategy

<a id="resq_mcp.dtsop.run_simulation"></a>

## run\_simulation

<a id="resq_mcp.dtsop.models"></a>

# resq\_mcp.dtsop.models

DTSOP domain models for the ResQ MCP server.

<a id="resq_mcp.dtsop.models.annotations"></a>

## annotations

<a id="resq_mcp.dtsop.models.Literal"></a>

## Literal

<a id="resq_mcp.dtsop.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.dtsop.models.SimulationRequest"></a>

## SimulationRequest Objects

```python
class SimulationRequest(BaseModel)
```

Request for high-fidelity physics simulation in digital twin.

Part of DTSOP system. Triggers physics-based simulation in Unity/Unreal
Engine for accurate disaster propagation modeling and strategy validation.

**Attributes**:

- `scenario_id` - Unique scenario identifier for this simulation.
- `sector_id` - Geographic sector to simulate.
- `disaster_type` - Type of disaster to model (e.g., "flood", "wildfire").
- `parameters` - Simulation parameters (e.g., &#123;"wind_speed": 15.5, "water_level": 2.3&#125;).
- `priority` - Processing priority (standard queued, urgent fast-tracked).
  

**Notes**:

  Simulations run asynchronously. Monitor progress via the returned
  simulation ID and resource subscription (resq://simulations/&#123;id&#125;).

<a id="resq_mcp.dtsop.models.SimulationRequest.scenario_id"></a>

#### scenario\_id

<a id="resq_mcp.dtsop.models.SimulationRequest.sector_id"></a>

#### sector\_id

<a id="resq_mcp.dtsop.models.SimulationRequest.disaster_type"></a>

#### disaster\_type

<a id="resq_mcp.dtsop.models.SimulationRequest.parameters"></a>

#### parameters

e.g., wind_speed, water_level

<a id="resq_mcp.dtsop.models.SimulationRequest.priority"></a>

#### priority

<a id="resq_mcp.dtsop.models.OptimizationStrategy"></a>

## OptimizationStrategy Objects

```python
class OptimizationStrategy(BaseModel)
```

Reinforcement learning-optimized deployment and evacuation strategy.

Part of DTSOP system. Generated by RL agents trained on thousands of
simulated disaster scenarios to optimize resource allocation and
evacuation routing under various constraints.

**Attributes**:

- `strategy_id` - Unique strategy identifier (e.g., "STRAT-X1Y2Z3W4").
- `related_alert_id` - Pre-alert or incident ID this strategy addresses.
- `recommended_deployment` - Mapping of drone types to recommended counts
  (e.g., &#123;"surveillance": 2, "payload": 1&#125;).
- `evacuation_routes` - Ordered list of recommended evacuation routes.
- `estimated_success_rate` - Predicted success probability (0.0 to 1.0)
  based on simulation outcomes.
- `simulation_proof_url` - NeoFS/IPFS URL for simulation evidence and logs.
  

**Notes**:

  Success rate derived from Monte Carlo simulations across varying
  disaster intensities and communication scenarios.

<a id="resq_mcp.dtsop.models.OptimizationStrategy.strategy_id"></a>

#### strategy\_id

<a id="resq_mcp.dtsop.models.OptimizationStrategy.related_alert_id"></a>

#### related\_alert\_id

<a id="resq_mcp.dtsop.models.OptimizationStrategy.recommended_deployment"></a>

#### recommended\_deployment

drone_type -> count

<a id="resq_mcp.dtsop.models.OptimizationStrategy.evacuation_routes"></a>

#### evacuation\_routes

<a id="resq_mcp.dtsop.models.OptimizationStrategy.estimated_success_rate"></a>

#### estimated\_success\_rate

<a id="resq_mcp.dtsop.models.OptimizationStrategy.simulation_proof_url"></a>

#### simulation\_proof\_url

<a id="resq_mcp.dtsop.service"></a>

# resq\_mcp.dtsop.service

DTSOP - Digital Twin Simulation & Optimization Platform.

This module provides simulation and optimization capabilities:
- High-fidelity physics simulation triggering (Unity/Unreal Engine integration)
- RL-optimized drone deployment strategies
- Evacuation route generation

The current implementation is stubbed for development and returns simulated data.

<a id="resq_mcp.dtsop.service.annotations"></a>

## annotations

<a id="resq_mcp.dtsop.service.random"></a>

## random

<a id="resq_mcp.dtsop.service.uuid"></a>

## uuid

<a id="resq_mcp.dtsop.service.Final"></a>

## Final

<a id="resq_mcp.dtsop.service.OptimizationStrategy"></a>

## OptimizationStrategy

<a id="resq_mcp.dtsop.service.SimulationRequest"></a>

## SimulationRequest

<a id="resq_mcp.dtsop.service.run_simulation"></a>

#### run\_simulation

```python
def run_simulation(request: SimulationRequest) -> str
```

Trigger a high-fidelity physics simulation in the digital twin.

Part of DTSOP (Digital Twin Simulation & Optimization Platform) system.
Queues a physics simulation job for async processing by Unity/Unreal
Engine with PX4 SITL and Gazebo integration.

Simulation Capabilities:
- Disaster propagation physics (flood spread, fire dynamics)
- Drone swarm dynamics and collision avoidance
- Communication link degradation under disaster conditions
- Infrastructure failure cascades
- Population movement and evacuation modeling

**Arguments**:

- `request` - Simulation parameters including:
  - scenario_id: Unique identifier for this simulation run
  - sector_id: Geographic area to simulate
  - disaster_type: Physics model to apply (flood/wildfire/earthquake)
  - parameters: Scenario-specific params (wind speed, water level, etc.)
  - priority: "standard" (queued) or "urgent" (fast-tracked)
  

**Returns**:

- `str` - Unique simulation job ID (format: "SIM-XXXXXXXX" where X is hex).
  Use this ID to monitor progress via resq://simulations/&#123;id&#125; resource.
  

**Example**:

  >>> from resq_mcp.dtsop.models import SimulationRequest
  >>> req = SimulationRequest(
  ...     scenario_id="flood-scenario-001",
  ...     sector_id="Sector-1",
  ...     disaster_type="flood",
  ...     parameters=&#123;"water_level": 2.5, "flow_rate": 1.2&#125;,
  ...     priority="urgent"
  ... )
  >>> sim_id = run_simulation(req)
  >>> print(f"Simulation queued: &#123;sim_id&#125;")
  
  Integration Note:
  Production implementation would:
  1. Validate request against available simulation templates
  2. Queue job to Unity/Unreal Engine processing cluster
  3. Store simulation state in Redis for progress tracking
  4. Send SSE notifications on status changes
  5. Store results (JSON + video) to NeoFS with CID

<a id="resq_mcp.dtsop.service.get_optimization_strategy"></a>

#### get\_optimization\_strategy

```python
def get_optimization_strategy(
        incident_or_alert_id: str) -> OptimizationStrategy
```

Generate RL-optimized deployment and evacuation strategy.

Part of DTSOP system. Uses reinforcement learning agents trained on
thousands of simulated scenarios to recommend optimal resource allocation
and routing under constraints (battery, weather, infrastructure damage).

Strategy Components:
- Recommended drone deployment mix (surveillance, payload, relay types)
- Evacuation route prioritization based on congestion and safety
- Success probability from Monte Carlo simulation ensemble
- Blockchain-linked proof for audit trail

RL Agent Training:
- Reward function: Lives saved + Response time + Resource efficiency
- State space: Disaster extent, infrastructure status, drone positions
- Action space: Deployment counts, waypoint routing, risk thresholds
- Training: PPO algorithm on 100k+ simulated disaster scenarios

**Arguments**:

- `incident_or_alert_id` - The incident ID (INC-XXX) or pre-alert ID (PRE-XXX)
  to optimize strategy for.
  

**Returns**:

- `OptimizationStrategy` - Complete strategy including:
  - strategy_id: Unique identifier for this strategy
  - recommended_deployment: Drone type to count mapping
  - evacuation_routes: Ordered list of recommended routes
  - estimated_success_rate: Predicted success (0.0-1.0)
  - simulation_proof_url: NeoFS link to simulation evidence
  

**Example**:

  >>> strategy = get_optimization_strategy("PRE-ABC123")
  >>> print(f"Strategy: &#123;strategy.strategy_id&#125;")
  >>> print(f"Deployment: &#123;strategy.recommended_deployment&#125;")
  >>> print(f"Success rate: &#123;strategy.estimated_success_rate:.0%&#125;")
  >>> for route in strategy.evacuation_routes:
  ...     print(f"Route: &#123;route&#125;")
  

**Notes**:

  Current implementation randomly selects from predefined templates.
  Production would invoke actual RL agent inference with real-time data.

<a id="resq_mcp.dtsop.tools"></a>

# resq\_mcp.dtsop.tools

MCP tool wrappers for DTSOP domain.

<a id="resq_mcp.dtsop.tools.logging"></a>

## logging

<a id="resq_mcp.dtsop.tools.UTC"></a>

## UTC

<a id="resq_mcp.dtsop.tools.datetime"></a>

## datetime

<a id="resq_mcp.dtsop.tools.Context"></a>

## Context

<a id="resq_mcp.dtsop.tools.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.dtsop.tools.OptimizationStrategy"></a>

## OptimizationStrategy

<a id="resq_mcp.dtsop.tools.SimulationRequest"></a>

## SimulationRequest

<a id="resq_mcp.dtsop.tools.get_optimization_strategy"></a>

## get\_optimization\_strategy

<a id="resq_mcp.dtsop.tools.trigger_sim"></a>

## trigger\_sim

<a id="resq_mcp.dtsop.tools.MAX_SIMULATIONS"></a>

## MAX\_SIMULATIONS

<a id="resq_mcp.dtsop.tools.incidents"></a>

## incidents

<a id="resq_mcp.dtsop.tools.mcp"></a>

## mcp

<a id="resq_mcp.dtsop.tools.simulations"></a>

## simulations

<a id="resq_mcp.dtsop.tools.logger"></a>

#### logger

<a id="resq_mcp.dtsop.tools.run_simulation"></a>

#### run\_simulation

```python
@mcp.tool()
async def run_simulation(request: SimulationRequest,
                         ctx: Context | None = None) -> str
```

Trigger a Digital Twin physics simulation for disaster scenario modeling.

Queues a high-fidelity simulation job and returns immediately with a
job ID. Clients should subscribe to the simulation resource URI for
real-time progress updates and result notification.

Workflow:
1. Validate simulation request parameters
2. Generate unique simulation ID
3. Queue job to DTSOP backend (Unity/Unreal Engine)
4. Store job metadata in simulation registry
5. Return simulation ID and subscription URI
6. Background processor updates status -> processing -> completed
7. Client fetches results from NeoFS when completed

**Arguments**:

- `request` - SimulationRequest with:
  - scenario_id: Unique scenario identifier
  - sector_id: Geographic sector to simulate
  - disaster_type: Physics model (flood/wildfire/earthquake)
  - parameters: Scenario params (wind_speed, water_level, etc.)
  - priority: "standard" or "urgent"
- `ctx` - Optional FastMCP context for logging.
  

**Returns**:

- `str` - Message with simulation ID and subscription instructions:
  "Simulation queued with ID: SIM-XXXXXXXX.
  Subscribe to resq://simulations/SIM-XXXXXXXX for updates."
  

**Example**:

  >>> from resq_mcp.dtsop.models import SimulationRequest
  >>> request = SimulationRequest(
  ...     scenario_id="flood-001",
  ...     sector_id="Sector-1",
  ...     disaster_type="flood",
  ...     parameters=&#123;"water_level": 2.5&#125;,
  ...     priority="urgent"
  ... )
  >>> result = await run_simulation(request)
  >>> print(result)  # "Simulation queued with ID: SIM-ABCD1234..."
  
  Integration:
  Production would:
  - Validate request against simulation templates
  - Check cluster capacity and queue position
  - Store job in Redis with priority
  - Submit to Unity/Unreal Engine processing cluster
  - Return estimated completion time

<a id="resq_mcp.dtsop.tools.get_deployment_strategy"></a>

#### get\_deployment\_strategy

```python
@mcp.tool()
async def get_deployment_strategy(incident_id: str) -> OptimizationStrategy
```

Generate an RL-optimized drone deployment and evacuation strategy.

Uses reinforcement learning models trained on thousands of simulated
disasters to recommend optimal resource allocation, routing, and
risk parameters for a specific incident or pre-alert.

**Arguments**:

- `incident_id` - Incident identifier (INC-XXX) or pre-alert ID (PRE-XXX)
  to generate strategy for.
  

**Returns**:

- `OptimizationStrategy` - Complete strategy recommendation with:
  - strategy_id: Unique identifier
  - related_alert_id: Original incident/alert ID
  - recommended_deployment: Drone type counts
  - evacuation_routes: Prioritized route list
  - estimated_success_rate: Predicted success (0.0-1.0)
  - simulation_proof_url: NeoFS evidence link
  

**Example**:

  >>> strategy = await get_deployment_strategy("PRE-ABC123")
  >>> print(strategy.strategy_id)
  >>> print(strategy.recommended_deployment)  # &#123;"surveillance": 2, ...&#125;
  >>> print(f"Success rate: &#123;strategy.estimated_success_rate:.0%&#125;")
  
  Use Cases:
  - Pre-positioning drones before predicted disasters (PDIE alerts)
  - Active response optimization for confirmed incidents
  - Multi-objective optimization (speed, safety, resource efficiency)
  - Scenario comparison and sensitivity analysis
  
  Integration:
  Strategy linked to blockchain for immutable audit trail.
  After approval, use update_mission_params to push to drones.

<a id="resq_mcp.hce"></a>

# resq\_mcp.hce

HCE - Hybrid Coordination Engine package.

<a id="resq_mcp.hce.annotations"></a>

## annotations

<a id="resq_mcp.hce.IncidentReport"></a>

## IncidentReport

<a id="resq_mcp.hce.IncidentValidation"></a>

## IncidentValidation

<a id="resq_mcp.hce.MissionParameters"></a>

## MissionParameters

<a id="resq_mcp.hce.update_mission_params"></a>

## update\_mission\_params

<a id="resq_mcp.hce.validate_incident"></a>

## validate\_incident

<a id="resq_mcp.hce.models"></a>

# resq\_mcp.hce.models

HCE domain models for the ResQ MCP server.

<a id="resq_mcp.hce.models.annotations"></a>

## annotations

<a id="resq_mcp.hce.models.datetime"></a>

## datetime

<a id="resq_mcp.hce.models.Literal"></a>

## Literal

<a id="resq_mcp.hce.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.hce.models.Field"></a>

## Field

<a id="resq_mcp.hce.models.IncidentReport"></a>

## IncidentReport Objects

```python
class IncidentReport(BaseModel)
```

Initial incident report from Edge AI, human observers, or sensors.

Part of HCE (Hybrid Coordination Engine) system. Represents unvalidated
incident detection requiring cross-reference and validation before
triggering full response protocols.

**Attributes**:

- `incident_id` - Unique incident identifier.
- `source` - Detection source (edge_ai=onboard processing, human_report=operator,
  sensor_network=ground sensors).
- `sector_id` - Geographic sector of the incident.
- `detected_type` - Incident classification (e.g., "fire", "collision", "flooding").
- `confidence` - Detection confidence from source (0.0 to 1.0).
- `evidence_url` - Optional URL to evidence (video, photos) on IPFS/NeoFS.
- `timestamp` - UTC timestamp of detection (auto-generated).
  

**Notes**:

  High-confidence reports (>0.85) may auto-confirm. Lower confidence
  reports cross-referenced with PDIE predictions and other sources.

<a id="resq_mcp.hce.models.IncidentReport.incident_id"></a>

#### incident\_id

<a id="resq_mcp.hce.models.IncidentReport.source"></a>

#### source

<a id="resq_mcp.hce.models.IncidentReport.sector_id"></a>

#### sector\_id

<a id="resq_mcp.hce.models.IncidentReport.detected_type"></a>

#### detected\_type

<a id="resq_mcp.hce.models.IncidentReport.confidence"></a>

#### confidence

<a id="resq_mcp.hce.models.IncidentReport.evidence_url"></a>

#### evidence\_url

<a id="resq_mcp.hce.models.IncidentReport.timestamp"></a>

#### timestamp

<a id="resq_mcp.hce.models.IncidentValidation"></a>

## IncidentValidation Objects

```python
class IncidentValidation(BaseModel)
```

Validation result after cross-referencing an incident report.

Part of HCE system. Produced after comparing incident reports against
PDIE predictions, sensor networks, and historical data to confirm
authenticity and trigger appropriate response protocols.

**Attributes**:

- `incident_id` - ID of the incident being validated.
- `is_confirmed` - Whether the incident is confirmed as genuine.
- `validation_source` - System or agent that performed validation
  (e.g., "SpoonOS-HCE-Validator", "Human-Operator").
- `correlated_pre_alert_id` - Related PDIE pre-alert if correlation found.
- `notes` - Detailed validation reasoning and cross-reference results.
  

**Example**:

  >>> validation = IncidentValidation(
  ...     incident_id="INC-123",
  ...     is_confirmed=True,
  ...     validation_source="SpoonOS-HCE-Validator",
  ...     notes="Confirmed via PDIE correlation and sensor data"
  ... )

<a id="resq_mcp.hce.models.IncidentValidation.incident_id"></a>

#### incident\_id

<a id="resq_mcp.hce.models.IncidentValidation.is_confirmed"></a>

#### is\_confirmed

<a id="resq_mcp.hce.models.IncidentValidation.validation_source"></a>

#### validation\_source

e.g., "SpoonOS-Validator"

<a id="resq_mcp.hce.models.IncidentValidation.correlated_pre_alert_id"></a>

#### correlated\_pre\_alert\_id

<a id="resq_mcp.hce.models.IncidentValidation.notes"></a>

#### notes

<a id="resq_mcp.hce.models.MissionParameters"></a>

## MissionParameters Objects

```python
class MissionParameters(BaseModel)
```

Authorized mission parameters pushed to drone via HCE.

Part of HCE system. Defines the authorized action space and risk
parameters for autonomous drone operations. Includes blockchain hash
for immutable audit trail of mission authorizations.

**Attributes**:

- `mission_id` - Unique mission identifier (e.g., "MISS-A1B2C3D4").
- `target_sector` - Assigned operational sector.
- `authorized_actions` - List of permitted autonomous actions
  (e.g., ["autonomous_flight", "payload_release_authorized"]).
- `risk_tolerance` - Maximum acceptable risk level (0.0 to 1.0).
  Lower values restrict aggressive maneuvers.
- `strategy_hash` - Blockchain transaction hash linking to strategy record
  for immutable audit trail (format: "0xHEXDIGITS").
- `timestamp` - UTC timestamp of parameter push (auto-generated).
  
  Security Note:
  Authorized actions are validated against drone firmware capabilities.
  Unauthorized actions are rejected by ResQ-OS security layer.

<a id="resq_mcp.hce.models.MissionParameters.mission_id"></a>

#### mission\_id

<a id="resq_mcp.hce.models.MissionParameters.target_sector"></a>

#### target\_sector

<a id="resq_mcp.hce.models.MissionParameters.authorized_actions"></a>

#### authorized\_actions

<a id="resq_mcp.hce.models.MissionParameters.risk_tolerance"></a>

#### risk\_tolerance

<a id="resq_mcp.hce.models.MissionParameters.strategy_hash"></a>

#### strategy\_hash

blockchain link

<a id="resq_mcp.hce.models.MissionParameters.timestamp"></a>

#### timestamp

<a id="resq_mcp.hce.service"></a>

# resq\_mcp.hce.service

HCE - Hybrid Coordination Engine.

This module provides incident validation and mission parameter management:
- Cross-reference Edge AI reports with other data sources
- Push authorized actions and risk parameters to drones
- Generate blockchain-linked strategy hashes for audit trails

The current implementation is stubbed for development and returns simulated data.

<a id="resq_mcp.hce.service.annotations"></a>

## annotations

<a id="resq_mcp.hce.service.hashlib"></a>

## hashlib

<a id="resq_mcp.hce.service.uuid"></a>

## uuid

<a id="resq_mcp.hce.service.TYPE_CHECKING"></a>

## TYPE\_CHECKING

<a id="resq_mcp.hce.service.Final"></a>

## Final

<a id="resq_mcp.hce.service.IncidentReport"></a>

## IncidentReport

<a id="resq_mcp.hce.service.IncidentValidation"></a>

## IncidentValidation

<a id="resq_mcp.hce.service.MissionParameters"></a>

## MissionParameters

<a id="resq_mcp.hce.service.validate_incident"></a>

#### validate\_incident

```python
def validate_incident(report: IncidentReport) -> IncidentValidation
```

Cross-reference and validate an incident report from Edge AI or other sources.

Part of HCE (Hybrid Coordination Engine) system. Prevents false positives
by validating reports against multiple data sources before triggering
full response protocols.

Validation Process:
1. Check report confidence level
- If confidence > 0.85: Auto-confirm (high-quality detection)
- If confidence <= 0.85: Cross-reference required
2. Cross-reference with (production):
- PDIE pre-alerts (was disaster predicted?)
- Other sector scans (spatial correlation)
- Historical incident patterns
- Ground sensor networks
3. Generate validation result with reasoning

Auto-Confirmation Threshold:
Reports with confidence > 0.85 are auto-confirmed because:
- High-quality edge AI models (>95% precision on test set)
- Multi-sensor fusion (visual + thermal + LiDAR)
- Onboard confidence calibration

**Arguments**:

- `report` - Incident report containing:
  - incident_id: Unique identifier
  - source: Detection origin (edge_ai/human_report/sensor_network)
  - sector_id: Geographic location
  - detected_type: Incident classification
  - confidence: Detection confidence (0.0-1.0)
  - evidence_url: Optional IPFS/NeoFS evidence link
  

**Returns**:

- `IncidentValidation` - Validation result with:
  - incident_id: Original incident ID
  - is_confirmed: True if validated, False if rejected
  - validation_source: System that performed validation
  - notes: Detailed reasoning for decision
  

**Example**:

  >>> from resq_mcp.hce.models import IncidentReport
  >>> report = IncidentReport(
  ...     incident_id="INC-123",
  ...     source="edge_ai",
  ...     sector_id="Sector-1",
  ...     detected_type="wildfire",
  ...     confidence=0.92,
  ...     evidence_url="neofs://evidence/fire_123.mp4"
  ... )
  >>> validation = validate_incident(report)
  >>> if validation.is_confirmed:
  ...     print("Incident confirmed - trigger response")
  

**Notes**:

  Current implementation uses simple threshold logic. Production
  would integrate with PDIE correlation engine and multi-source fusion.

<a id="resq_mcp.hce.service.update_mission_params"></a>

#### update\_mission\_params

```python
def update_mission_params(
        drone_id: str,
        strategy_id: str,
        is_urgent: bool = False) -> MissionParameters | ErrorResponse
```

Push new authorized mission parameters to a specific drone.

Part of HCE system. Defines the authorized action space and risk
parameters for autonomous drone operations following strategy approval.

Security Model:
- Each mission linked to blockchain strategy record (immutable audit)
- Authorized actions validated by ResQ-OS security layer on drone
- Risk tolerance enforced by flight controller firmware
- Unauthorized actions rejected before execution

Mission Parameters Include:
- Authorized actions: What the drone is permitted to do autonomously
(e.g., "autonomous_flight", "payload_release_authorized")
- Risk tolerance: Maximum acceptable risk (0.0-1.0)
- 0.9 = Urgent missions (aggressive routing, higher speeds)
- 0.5 = Standard missions (conservative, safety-first)
- Strategy hash: Blockchain transaction linking to strategy record
(format: "0x" + SHA256 hex digest)

**Arguments**:

- `drone_id` - Target drone identifier (e.g., "DRONE-Alpha").
  Used in production to route parameters to specific unit.
- `strategy_id` - Approved strategy identifier from DTSOP (e.g., "STRAT-X1Y2Z3").
  Used to generate blockchain hash and determine risk level.
  

**Returns**:

- `MissionParameters` - Complete parameter set with:
  - mission_id: Unique mission identifier
  - target_sector: Assigned operational area
  - authorized_actions: List of permitted autonomous actions
  - risk_tolerance: Risk threshold (0.0-1.0)
  - strategy_hash: Blockchain link (0xHEXDIGITS)
- `ErrorResponse` - Error if drone unavailable or strategy invalid (future).
  

**Example**:

  >>> params = update_mission_params(
  ...     drone_id="DRONE-Alpha",
  ...     strategy_id="STRAT-URGENT-FIRE"
  ... )
  >>> if isinstance(params, MissionParameters):
  ...     print(f"Mission: &#123;params.mission_id&#125;")
  ...     print(f"Actions: &#123;params.authorized_actions&#125;")
  ...     print(f"Risk: &#123;params.risk_tolerance&#125;")
  ...     print(f"Blockchain: &#123;params.strategy_hash&#125;")
  
  Blockchain Integration:
  Strategy hash links to Neo N3 transaction containing:
  - Strategy JSON (deployment plan, routes, success rate)
  - Simulation proof CID (IPFS/NeoFS evidence)
  - Timestamp and approving authority
  - Provides immutable audit trail for post-incident review
  

**Notes**:

  Current implementation generates mock blockchain hash. Production
  would submit actual transaction to Neo N3 testnet/mainnet.

<a id="resq_mcp.hce.tools"></a>

# resq\_mcp.hce.tools

MCP tool wrappers for HCE domain.

<a id="resq_mcp.hce.tools.logging"></a>

## logging

<a id="resq_mcp.hce.tools.time"></a>

## time

<a id="resq_mcp.hce.tools.UTC"></a>

## UTC

<a id="resq_mcp.hce.tools.datetime"></a>

## datetime

<a id="resq_mcp.hce.tools.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.hce.tools.IncidentValidation"></a>

## IncidentValidation

<a id="resq_mcp.hce.tools.MissionParameters"></a>

## MissionParameters

<a id="resq_mcp.hce.tools.MAX_INCIDENTS"></a>

## MAX\_INCIDENTS

<a id="resq_mcp.hce.tools.MAX_MISSIONS"></a>

## MAX\_MISSIONS

<a id="resq_mcp.hce.tools.incidents"></a>

## incidents

<a id="resq_mcp.hce.tools.mcp"></a>

## mcp

<a id="resq_mcp.hce.tools.missions"></a>

## missions

<a id="resq_mcp.hce.tools.logger"></a>

#### logger

<a id="resq_mcp.hce.tools.validate_incident"></a>

#### validate\_incident

```python
@mcp.tool()
async def validate_incident(val: IncidentValidation) -> str
```

Submit validation result for an incident report.

Used by human operators or automated validation systems (HCE) to
confirm or reject incident reports before triggering full response.

**Arguments**:

- `val` - IncidentValidation with:
  - incident_id: ID of incident being validated
  - is_confirmed: True=confirmed, False=rejected/false positive
  - validation_source: Who/what validated (e.g., "Human-Operator")
  - correlated_pre_alert_id: Optional linked PDIE alert
  - notes: Validation reasoning and evidence
  

**Returns**:

- `str` - Confirmation message indicating action taken:
  "Incident &#123;id&#125; successfully CONFIRMED." or
  "Incident &#123;id&#125; successfully REJECTED."
  

**Example**:

  >>> from resq_mcp.hce.models import IncidentValidation
  >>> validation = IncidentValidation(
  ...     incident_id="INC-123",
  ...     is_confirmed=True,
  ...     validation_source="Human-Operator-Alice",
  ...     notes="Confirmed via video evidence and ground reports"
  ... )
  >>> result = await validate_incident(validation)
  >>> print(result)  # "Incident INC-123 successfully CONFIRMED."
  
  Workflow:
  1. Edge AI detects incident (low confidence)
  2. HCE cross-references with PDIE/sensors
  3. If ambiguous -> human review required
  4. Operator submits validation via this tool
  5. If confirmed -> trigger response strategy
  6. If rejected -> log as false positive, update ML model
  
  Audit Trail:
  All validations logged with timestamp, source, and reasoning
  for post-incident analysis and ML model refinement.

<a id="resq_mcp.hce.tools.update_mission_params"></a>

#### update\_mission\_params

```python
@mcp.tool()
async def update_mission_params(drone_id: str,
                                strategy_id: str,
                                is_urgent: bool = False) -> MissionParameters
```

Push authorized mission parameters to a drone for an approved strategy.

Completes the deployment workflow after a strategy has been approved:
get_deployment_strategy -> (human approval) -> update_mission_params -> drone executes.

**Arguments**:

- `drone_id` - Target drone identifier (e.g., "DRONE-Alpha").
- `strategy_id` - Approved strategy ID from get_deployment_strategy (e.g., "STRAT-X1Y2Z3").
- `is_urgent` - If True, sets risk_tolerance=0.9 (aggressive routing) instead of the
  default 0.5. Must be explicitly set — urgency is never derived from the
  strategy_id string to prevent injection attacks.
  

**Returns**:

- `MissionParameters` - Authorized parameter set including mission ID, allowed actions,
  risk tolerance, and a deterministic blockchain-anchored strategy hash.
  

**Raises**:

- `FastMCPError` - If the drone already has an active mission for a different strategy
  (conflict guard), or if the mission store is at capacity.
  

**Example**:

  >>> params = await update_mission_params("DRONE-Alpha", "STRAT-ABCD1234", is_urgent=True)
  >>> print(params.authorized_actions)
  >>> print(params.strategy_hash)  # 0xSHA256(strategy_id:mission_id)

<a id="resq_mcp.models"></a>

# resq\_mcp.models

Domain models for the ResQ MCP server.

These Pydantic models define the core data contracts for the three main subsystems:
- PDIE (Predictive Disaster Intelligence Engine)
- DTSOP (Digital Twin Simulation & Optimization Platform)
- HCE (Hybrid Coordination Engine)

All datetime fields use timezone-aware UTC timestamps for consistency across
distributed systems and audit logging.

<a id="resq_mcp.models.annotations"></a>

## annotations

<a id="resq_mcp.models.UTC"></a>

## UTC

<a id="resq_mcp.models.datetime"></a>

## datetime

<a id="resq_mcp.models.Literal"></a>

## Literal

<a id="resq_mcp.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.models.Field"></a>

## Field

<a id="resq_mcp.models.Coordinates"></a>

## Coordinates Objects

```python
class Coordinates(BaseModel)
```

Geographic coordinates with status indicator.

Represents a geographic point in decimal degrees (WGS84 datum)
with an associated status flag for monitoring.

**Attributes**:

- `lat` - Latitude in decimal degrees (-90 to +90).
- `lng` - Longitude in decimal degrees (-180 to +180).
- `status` - Current status indicator (e.g., "clear", "critical").
  

**Example**:

  >>> coords = Coordinates(lat=37.3417, lng=-121.9751, status="clear")
  >>> print(f"Position: &#123;coords.lat&#125;, &#123;coords.lng&#125;")

<a id="resq_mcp.models.Coordinates.lat"></a>

#### lat

<a id="resq_mcp.models.Coordinates.lng"></a>

#### lng

<a id="resq_mcp.models.Coordinates.status"></a>

#### status

<a id="resq_mcp.models.Sector"></a>

## Sector Objects

```python
class Sector(BaseModel)
```

A monitored geographic sector in the drone surveillance network.

Sectors are predefined geographic zones monitored by the drone fleet
for disaster detection and response coordination.

**Attributes**:

- `id` - Unique sector identifier (e.g., "Sector-1").
- `coordinates` - Center point coordinates with status.

<a id="resq_mcp.models.Sector.id"></a>

#### id

<a id="resq_mcp.models.Sector.coordinates"></a>

#### coordinates

<a id="resq_mcp.models.DetectedObject"></a>

## DetectedObject Objects

```python
class DetectedObject(BaseModel)
```

An object detected by drone sensors during surveillance.

Represents the output of edge AI object detection running on drone
hardware or ground processing stations.

**Attributes**:

- `name` - Human-readable name of detected object (default: "None").
- `type` - Classification type (e.g., "fire", "vehicle", "person").
- `confidence` - Detection confidence score (0.0 to 1.0).
- `description` - Detailed description of the detection.

<a id="resq_mcp.models.DetectedObject.name"></a>

#### name

<a id="resq_mcp.models.DetectedObject.type"></a>

#### type

<a id="resq_mcp.models.DetectedObject.confidence"></a>

#### confidence

<a id="resq_mcp.models.DetectedObject.description"></a>

#### description

<a id="resq_mcp.models.DisasterScenario"></a>

## DisasterScenario Objects

```python
class DisasterScenario(BaseModel)
```

A disaster scenario template for simulation and detection.

Defines the characteristics of a disaster type that can be detected
by drone surveillance or used as input for digital twin simulations.

**Attributes**:

- `type` - Disaster category (e.g., "wildfire", "flood", "earthquake").
- `name` - Human-readable scenario name.
- `confidence` - Detection confidence or scenario likelihood (0.0 to 1.0).
- `description` - Detailed scenario description including characteristics.

<a id="resq_mcp.models.DisasterScenario.type"></a>

#### type

<a id="resq_mcp.models.DisasterScenario.name"></a>

#### name

<a id="resq_mcp.models.DisasterScenario.confidence"></a>

#### confidence

<a id="resq_mcp.models.DisasterScenario.description"></a>

#### description

<a id="resq_mcp.models.SectorAnalysis"></a>

## SectorAnalysis Objects

```python
class SectorAnalysis(BaseModel)
```

Complete analysis result from a sector surveillance scan.

Contains all detection data, evidence links, and recommended actions
from a drone sector scan. Used for incident reporting and blockchain
evidence submission.

**Attributes**:

- `sector_id` - Identifier of the scanned sector.
- `timestamp` - UTC timestamp of the analysis (auto-generated).
- `status` - Overall status (e.g., "clear", "CRITICAL_ALERT").
- `detected_object` - Primary object or hazard detected.
- `disaster_type` - Classified disaster type if applicable.
- `confidence` - Detection confidence score (0.0 to 1.0).
- `description` - Detailed analysis description.
- `coordinates` - Geographic coordinates of the detection.
- `video_proof_url` - NeoFS/IPFS URL for video evidence.
- `recommended_action` - Suggested next action (e.g., "IMMEDIATE_REPORT_TO_BLOCKCHAIN").

<a id="resq_mcp.models.SectorAnalysis.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.SectorAnalysis.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.SectorAnalysis.status"></a>

#### status

<a id="resq_mcp.models.SectorAnalysis.detected_object"></a>

#### detected\_object

<a id="resq_mcp.models.SectorAnalysis.disaster_type"></a>

#### disaster\_type

<a id="resq_mcp.models.SectorAnalysis.confidence"></a>

#### confidence

<a id="resq_mcp.models.SectorAnalysis.description"></a>

#### description

<a id="resq_mcp.models.SectorAnalysis.coordinates"></a>

#### coordinates

<a id="resq_mcp.models.SectorAnalysis.video_proof_url"></a>

#### video\_proof\_url

<a id="resq_mcp.models.SectorAnalysis.recommended_action"></a>

#### recommended\_action

<a id="resq_mcp.models.SectorStatusSummary"></a>

## SectorStatusSummary Objects

```python
class SectorStatusSummary(BaseModel)
```

Condensed status summary for network-wide sector monitoring.

Lightweight representation used in network status dashboards and
overview displays. Excludes detailed evidence and coordinates.

**Attributes**:

- `status` - Current sector status indicator.
- `detected_object` - Primary detected object or "None".
- `confidence` - Overall confidence score for the status.

<a id="resq_mcp.models.SectorStatusSummary.status"></a>

#### status

<a id="resq_mcp.models.SectorStatusSummary.detected_object"></a>

#### detected\_object

<a id="resq_mcp.models.SectorStatusSummary.confidence"></a>

#### confidence

<a id="resq_mcp.models.NetworkStatus"></a>

## NetworkStatus Objects

```python
class NetworkStatus(BaseModel)
```

Aggregate status of the entire drone surveillance network.

Provides a network-wide view of all monitored sectors and critical
alert counts for operator dashboards and system health monitoring.

**Attributes**:

- `timestamp` - UTC timestamp of the status snapshot (auto-generated).
- `total_sectors` - Total number of monitored sectors.
- `sectors` - Mapping of sector IDs to their status summaries.
- `critical_alerts` - Count of sectors with critical alerts active.

<a id="resq_mcp.models.NetworkStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.NetworkStatus.total_sectors"></a>

#### total\_sectors

<a id="resq_mcp.models.NetworkStatus.sectors"></a>

#### sectors

<a id="resq_mcp.models.NetworkStatus.critical_alerts"></a>

#### critical\_alerts

<a id="resq_mcp.models.SwarmStatus"></a>

## SwarmStatus Objects

```python
class SwarmStatus(BaseModel)
```

Real-time operational status of the drone swarm.

Aggregates health metrics across all drones in the fleet including
battery levels, connectivity status, and deployment state.

**Attributes**:

- `timestamp` - UTC timestamp of the status snapshot (auto-generated).
- `total_drones` - Total number of drones in the fleet.
- `active_drones` - Number of drones currently deployed and operational.
- `average_battery` - Fleet-wide average battery percentage (0-100).
- `network_status` - Overall network health (e.g., "operational", "degraded").
- `last_sync` - UTC timestamp of last successful sync with ground station.

<a id="resq_mcp.models.SwarmStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.SwarmStatus.total_drones"></a>

#### total\_drones

<a id="resq_mcp.models.SwarmStatus.active_drones"></a>

#### active\_drones

<a id="resq_mcp.models.SwarmStatus.average_battery"></a>

#### average\_battery

<a id="resq_mcp.models.SwarmStatus.network_status"></a>

#### network\_status

<a id="resq_mcp.models.SwarmStatus.last_sync"></a>

#### last\_sync

<a id="resq_mcp.models.DeploymentRequest"></a>

## DeploymentRequest Objects

```python
class DeploymentRequest(BaseModel)
```

Request for immediate drone deployment to a specific sector.

Used by operators or automated systems to request drone dispatch
to sectors requiring surveillance or emergency response.

**Attributes**:

- `sector_id` - Target sector identifier for deployment.
- `priority` - Deployment urgency level (low/medium/high/critical).
  Higher priority requests preempt lower priority missions.

<a id="resq_mcp.models.DeploymentRequest.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.DeploymentRequest.priority"></a>

#### priority

<a id="resq_mcp.models.DeploymentStatus"></a>

## DeploymentStatus Objects

```python
class DeploymentStatus(BaseModel)
```

Response status for a drone deployment request.

Provides confirmation and tracking information for a deployment request
including assigned drone and estimated arrival time.

**Attributes**:

- `status` - Deployment state (e.g., "deployed", "en_route", "completed").
- `sector_id` - Target sector identifier.
- `priority` - Assigned priority level.
- `drone_id` - Identifier of the assigned drone unit.
- `eta_seconds` - Estimated time to arrival in seconds.
- `timestamp` - UTC timestamp of the status update (auto-generated).

<a id="resq_mcp.models.DeploymentStatus.status"></a>

#### status

<a id="resq_mcp.models.DeploymentStatus.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.DeploymentStatus.priority"></a>

#### priority

<a id="resq_mcp.models.DeploymentStatus.drone_id"></a>

#### drone\_id

<a id="resq_mcp.models.DeploymentStatus.eta_seconds"></a>

#### eta\_seconds

<a id="resq_mcp.models.DeploymentStatus.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.VulnerabilityMap"></a>

## VulnerabilityMap Objects

```python
class VulnerabilityMap(BaseModel)
```

Static vulnerability assessment data for a geographic sector.

Part of PDIE (Predictive Disaster Intelligence Engine) system.
Contains precomputed risk factors, infrastructure data, and population
metrics used for predictive disaster modeling and resource allocation.

**Attributes**:

- `sector_id` - Sector identifier this map applies to.
- `population_density` - Human population density category.
- `critical_infrastructure` - List of critical facilities (e.g., "hospital", "power-substation").
- `flood_risk` - Flood vulnerability score (0.0 to 1.0).
- `fire_risk` - Fire vulnerability score (0.0 to 1.0).
- `last_updated` - UTC timestamp of last data update (auto-generated).
  

**Notes**:

  Risk scores are precomputed from historical data, terrain analysis,
  and infrastructure density. Updated periodically via GIS integration.

<a id="resq_mcp.models.VulnerabilityMap.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.VulnerabilityMap.population_density"></a>

#### population\_density

<a id="resq_mcp.models.VulnerabilityMap.critical_infrastructure"></a>

#### critical\_infrastructure

<a id="resq_mcp.models.VulnerabilityMap.flood_risk"></a>

#### flood\_risk

<a id="resq_mcp.models.VulnerabilityMap.fire_risk"></a>

#### fire\_risk

<a id="resq_mcp.models.VulnerabilityMap.last_updated"></a>

#### last\_updated

<a id="resq_mcp.models.PreAlert"></a>

## PreAlert Objects

```python
class PreAlert(BaseModel)
```

Probabilistic disaster forecast from LSTM/GNN predictive models.

Part of PDIE system. Generated by machine learning models that analyze
weather patterns, sensor data, and historical trends to predict potential
disasters before they occur. Enables proactive resource positioning.

**Attributes**:

- `alert_id` - Unique alert identifier (e.g., "PRE-A1B2C3D4").
- `sector_id` - Target sector for the prediction.
- `predicted_disaster_type` - Expected disaster type (e.g., "wildfire", "flood").
- `probability` - Forecast confidence (0.0 to 1.0).
- `forecast_horizon_hours` - Time until predicted event (hours from now).
- `vulnerability_context` - Associated sector vulnerability data.
- `generated_at` - UTC timestamp of forecast generation (auto-generated).
  

**Example**:

  >>> alert = PreAlert(
  ...     alert_id="PRE-123ABC",
  ...     sector_id="Sector-1",
  ...     predicted_disaster_type="wildfire",
  ...     probability=0.85,
  ...     forecast_horizon_hours=12,
  ...     vulnerability_context=vuln_map
  ... )

<a id="resq_mcp.models.PreAlert.alert_id"></a>

#### alert\_id

<a id="resq_mcp.models.PreAlert.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.PreAlert.predicted_disaster_type"></a>

#### predicted\_disaster\_type

<a id="resq_mcp.models.PreAlert.probability"></a>

#### probability

<a id="resq_mcp.models.PreAlert.forecast_horizon_hours"></a>

#### forecast\_horizon\_hours

<a id="resq_mcp.models.PreAlert.vulnerability_context"></a>

#### vulnerability\_context

<a id="resq_mcp.models.PreAlert.generated_at"></a>

#### generated\_at

<a id="resq_mcp.models.SimulationRequest"></a>

## SimulationRequest Objects

```python
class SimulationRequest(BaseModel)
```

Request for high-fidelity physics simulation in digital twin.

Part of DTSOP system. Triggers physics-based simulation in Unity/Unreal
Engine for accurate disaster propagation modeling and strategy validation.

**Attributes**:

- `scenario_id` - Unique scenario identifier for this simulation.
- `sector_id` - Geographic sector to simulate.
- `disaster_type` - Type of disaster to model (e.g., "flood", "wildfire").
- `parameters` - Simulation parameters (e.g., &#123;"wind_speed": 15.5, "water_level": 2.3&#125;).
- `priority` - Processing priority (standard queued, urgent fast-tracked).
  

**Notes**:

  Simulations run asynchronously. Monitor progress via the returned
  simulation ID and resource subscription (resq://simulations/&#123;id&#125;).

<a id="resq_mcp.models.SimulationRequest.scenario_id"></a>

#### scenario\_id

<a id="resq_mcp.models.SimulationRequest.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.SimulationRequest.disaster_type"></a>

#### disaster\_type

<a id="resq_mcp.models.SimulationRequest.parameters"></a>

#### parameters

e.g., wind_speed, water_level

<a id="resq_mcp.models.SimulationRequest.priority"></a>

#### priority

<a id="resq_mcp.models.OptimizationStrategy"></a>

## OptimizationStrategy Objects

```python
class OptimizationStrategy(BaseModel)
```

Reinforcement learning-optimized deployment and evacuation strategy.

Part of DTSOP system. Generated by RL agents trained on thousands of
simulated disaster scenarios to optimize resource allocation and
evacuation routing under various constraints.

**Attributes**:

- `strategy_id` - Unique strategy identifier (e.g., "STRAT-X1Y2Z3W4").
- `related_alert_id` - Pre-alert or incident ID this strategy addresses.
- `recommended_deployment` - Mapping of drone types to recommended counts
  (e.g., &#123;"surveillance": 2, "payload": 1&#125;).
- `evacuation_routes` - Ordered list of recommended evacuation routes.
- `estimated_success_rate` - Predicted success probability (0.0 to 1.0)
  based on simulation outcomes.
- `simulation_proof_url` - NeoFS/IPFS URL for simulation evidence and logs.
  

**Notes**:

  Success rate derived from Monte Carlo simulations across varying
  disaster intensities and communication scenarios.

<a id="resq_mcp.models.OptimizationStrategy.strategy_id"></a>

#### strategy\_id

<a id="resq_mcp.models.OptimizationStrategy.related_alert_id"></a>

#### related\_alert\_id

<a id="resq_mcp.models.OptimizationStrategy.recommended_deployment"></a>

#### recommended\_deployment

drone_type -> count

<a id="resq_mcp.models.OptimizationStrategy.evacuation_routes"></a>

#### evacuation\_routes

<a id="resq_mcp.models.OptimizationStrategy.estimated_success_rate"></a>

#### estimated\_success\_rate

<a id="resq_mcp.models.OptimizationStrategy.simulation_proof_url"></a>

#### simulation\_proof\_url

<a id="resq_mcp.models.IncidentReport"></a>

## IncidentReport Objects

```python
class IncidentReport(BaseModel)
```

Initial incident report from Edge AI, human observers, or sensors.

Part of HCE (Hybrid Coordination Engine) system. Represents unvalidated
incident detection requiring cross-reference and validation before
triggering full response protocols.

**Attributes**:

- `incident_id` - Unique incident identifier.
- `source` - Detection source (edge_ai=onboard processing, human_report=operator,
  sensor_network=ground sensors).
- `sector_id` - Geographic sector of the incident.
- `detected_type` - Incident classification (e.g., "fire", "collision", "flooding").
- `confidence` - Detection confidence from source (0.0 to 1.0).
- `evidence_url` - Optional URL to evidence (video, photos) on IPFS/NeoFS.
- `timestamp` - UTC timestamp of detection (auto-generated).
  

**Notes**:

  High-confidence reports (>0.85) may auto-confirm. Lower confidence
  reports cross-referenced with PDIE predictions and other sources.

<a id="resq_mcp.models.IncidentReport.incident_id"></a>

#### incident\_id

<a id="resq_mcp.models.IncidentReport.source"></a>

#### source

<a id="resq_mcp.models.IncidentReport.sector_id"></a>

#### sector\_id

<a id="resq_mcp.models.IncidentReport.detected_type"></a>

#### detected\_type

<a id="resq_mcp.models.IncidentReport.confidence"></a>

#### confidence

<a id="resq_mcp.models.IncidentReport.evidence_url"></a>

#### evidence\_url

<a id="resq_mcp.models.IncidentReport.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.IncidentValidation"></a>

## IncidentValidation Objects

```python
class IncidentValidation(BaseModel)
```

Validation result after cross-referencing an incident report.

Part of HCE system. Produced after comparing incident reports against
PDIE predictions, sensor networks, and historical data to confirm
authenticity and trigger appropriate response protocols.

**Attributes**:

- `incident_id` - ID of the incident being validated.
- `is_confirmed` - Whether the incident is confirmed as genuine.
- `validation_source` - System or agent that performed validation
  (e.g., "SpoonOS-HCE-Validator", "Human-Operator").
- `correlated_pre_alert_id` - Related PDIE pre-alert if correlation found.
- `notes` - Detailed validation reasoning and cross-reference results.
  

**Example**:

  >>> validation = IncidentValidation(
  ...     incident_id="INC-123",
  ...     is_confirmed=True,
  ...     validation_source="SpoonOS-HCE-Validator",
  ...     notes="Confirmed via PDIE correlation and sensor data"
  ... )

<a id="resq_mcp.models.IncidentValidation.incident_id"></a>

#### incident\_id

<a id="resq_mcp.models.IncidentValidation.is_confirmed"></a>

#### is\_confirmed

<a id="resq_mcp.models.IncidentValidation.validation_source"></a>

#### validation\_source

e.g., "SpoonOS-Validator"

<a id="resq_mcp.models.IncidentValidation.correlated_pre_alert_id"></a>

#### correlated\_pre\_alert\_id

<a id="resq_mcp.models.IncidentValidation.notes"></a>

#### notes

<a id="resq_mcp.models.MissionParameters"></a>

## MissionParameters Objects

```python
class MissionParameters(BaseModel)
```

Authorized mission parameters pushed to drone via HCE.

Part of HCE system. Defines the authorized action space and risk
parameters for autonomous drone operations. Includes blockchain hash
for immutable audit trail of mission authorizations.

**Attributes**:

- `mission_id` - Unique mission identifier (e.g., "MISS-A1B2C3D4").
- `target_sector` - Assigned operational sector.
- `authorized_actions` - List of permitted autonomous actions
  (e.g., ["autonomous_flight", "payload_release_authorized"]).
- `risk_tolerance` - Maximum acceptable risk level (0.0 to 1.0).
  Lower values restrict aggressive maneuvers.
- `strategy_hash` - Blockchain transaction hash linking to strategy record
  for immutable audit trail (format: "0xHEXDIGITS").
- `timestamp` - UTC timestamp of parameter push (auto-generated).
  
  Security Note:
  Authorized actions are validated against drone firmware capabilities.
  Unauthorized actions are rejected by ResQ-OS security layer.

<a id="resq_mcp.models.MissionParameters.mission_id"></a>

#### mission\_id

<a id="resq_mcp.models.MissionParameters.target_sector"></a>

#### target\_sector

<a id="resq_mcp.models.MissionParameters.authorized_actions"></a>

#### authorized\_actions

<a id="resq_mcp.models.MissionParameters.risk_tolerance"></a>

#### risk\_tolerance

<a id="resq_mcp.models.MissionParameters.strategy_hash"></a>

#### strategy\_hash

blockchain link

<a id="resq_mcp.models.MissionParameters.timestamp"></a>

#### timestamp

<a id="resq_mcp.models.ErrorResponse"></a>

## ErrorResponse Objects

```python
class ErrorResponse(BaseModel)
```

Standard error response for failed operations.

Used across all subsystems to provide consistent error messaging.
Returned instead of raising exceptions for expected error conditions
(e.g., invalid sector ID, missing data).

**Attributes**:

- `status` - Always "error" to distinguish from success responses.
- `message` - Human-readable error description.
  

**Example**:

  >>> error = ErrorResponse(message="Sector not found")
  >>> if isinstance(result, ErrorResponse):
  ...     print(f"Error: &#123;result.message&#125;")

<a id="resq_mcp.models.ErrorResponse.status"></a>

#### status

<a id="resq_mcp.models.ErrorResponse.message"></a>

#### message

<a id="resq_mcp.pdie"></a>

# resq\_mcp.pdie

PDIE - Predictive Disaster Intelligence Engine package.

<a id="resq_mcp.pdie.annotations"></a>

## annotations

<a id="resq_mcp.pdie.PreAlert"></a>

## PreAlert

<a id="resq_mcp.pdie.VulnerabilityMap"></a>

## VulnerabilityMap

<a id="resq_mcp.pdie.get_predictive_alerts"></a>

## get\_predictive\_alerts

<a id="resq_mcp.pdie.get_vulnerability_map"></a>

## get\_vulnerability\_map

<a id="resq_mcp.pdie.models"></a>

# resq\_mcp.pdie.models

PDIE domain models for the ResQ MCP server.

<a id="resq_mcp.pdie.models.annotations"></a>

## annotations

<a id="resq_mcp.pdie.models.datetime"></a>

## datetime

<a id="resq_mcp.pdie.models.Literal"></a>

## Literal

<a id="resq_mcp.pdie.models.BaseModel"></a>

## BaseModel

<a id="resq_mcp.pdie.models.Field"></a>

## Field

<a id="resq_mcp.pdie.models.VulnerabilityMap"></a>

## VulnerabilityMap Objects

```python
class VulnerabilityMap(BaseModel)
```

Static vulnerability assessment data for a geographic sector.

Part of PDIE (Predictive Disaster Intelligence Engine) system.
Contains precomputed risk factors, infrastructure data, and population
metrics used for predictive disaster modeling and resource allocation.

**Attributes**:

- `sector_id` - Sector identifier this map applies to.
- `population_density` - Human population density category.
- `critical_infrastructure` - List of critical facilities (e.g., "hospital", "power-substation").
- `flood_risk` - Flood vulnerability score (0.0 to 1.0).
- `fire_risk` - Fire vulnerability score (0.0 to 1.0).
- `last_updated` - UTC timestamp of last data update (auto-generated).
  

**Notes**:

  Risk scores are precomputed from historical data, terrain analysis,
  and infrastructure density. Updated periodically via GIS integration.

<a id="resq_mcp.pdie.models.VulnerabilityMap.sector_id"></a>

#### sector\_id

<a id="resq_mcp.pdie.models.VulnerabilityMap.population_density"></a>

#### population\_density

<a id="resq_mcp.pdie.models.VulnerabilityMap.critical_infrastructure"></a>

#### critical\_infrastructure

<a id="resq_mcp.pdie.models.VulnerabilityMap.flood_risk"></a>

#### flood\_risk

<a id="resq_mcp.pdie.models.VulnerabilityMap.fire_risk"></a>

#### fire\_risk

<a id="resq_mcp.pdie.models.VulnerabilityMap.last_updated"></a>

#### last\_updated

<a id="resq_mcp.pdie.models.PreAlert"></a>

## PreAlert Objects

```python
class PreAlert(BaseModel)
```

Probabilistic disaster forecast from LSTM/GNN predictive models.

Part of PDIE system. Generated by machine learning models that analyze
weather patterns, sensor data, and historical trends to predict potential
disasters before they occur. Enables proactive resource positioning.

**Attributes**:

- `alert_id` - Unique alert identifier (e.g., "PRE-A1B2C3D4").
- `sector_id` - Target sector for the prediction.
- `predicted_disaster_type` - Expected disaster type (e.g., "wildfire", "flood").
- `probability` - Forecast confidence (0.0 to 1.0).
- `forecast_horizon_hours` - Time until predicted event (hours from now).
- `vulnerability_context` - Associated sector vulnerability data.
- `generated_at` - UTC timestamp of forecast generation (auto-generated).
  

**Example**:

  >>> alert = PreAlert(
  ...     alert_id="PRE-123ABC",
  ...     sector_id="Sector-1",
  ...     predicted_disaster_type="wildfire",
  ...     probability=0.85,
  ...     forecast_horizon_hours=12,
  ...     vulnerability_context=vuln_map
  ... )

<a id="resq_mcp.pdie.models.PreAlert.alert_id"></a>

#### alert\_id

<a id="resq_mcp.pdie.models.PreAlert.sector_id"></a>

#### sector\_id

<a id="resq_mcp.pdie.models.PreAlert.predicted_disaster_type"></a>

#### predicted\_disaster\_type

<a id="resq_mcp.pdie.models.PreAlert.probability"></a>

#### probability

<a id="resq_mcp.pdie.models.PreAlert.forecast_horizon_hours"></a>

#### forecast\_horizon\_hours

<a id="resq_mcp.pdie.models.PreAlert.vulnerability_context"></a>

#### vulnerability\_context

<a id="resq_mcp.pdie.models.PreAlert.generated_at"></a>

#### generated\_at

<a id="resq_mcp.pdie.service"></a>

# resq\_mcp.pdie.service

PDIE - Predictive Disaster Intelligence Engine.

This module provides predictive disaster intelligence:
- Vulnerability mapping for sectors (population, infrastructure, risks)
- Probabilistic forecasts for disaster events
- Pre-alert generation based on LSTM/GNN model outputs

The current implementation is stubbed with mock data for development.

<a id="resq_mcp.pdie.service.annotations"></a>

## annotations

<a id="resq_mcp.pdie.service.random"></a>

## random

<a id="resq_mcp.pdie.service.uuid"></a>

## uuid

<a id="resq_mcp.pdie.service.Final"></a>

## Final

<a id="resq_mcp.pdie.service.ErrorResponse"></a>

## ErrorResponse

<a id="resq_mcp.pdie.service.PreAlert"></a>

## PreAlert

<a id="resq_mcp.pdie.service.VulnerabilityMap"></a>

## VulnerabilityMap

<a id="resq_mcp.pdie.service.VULNERABILITY_DB"></a>

#### VULNERABILITY\_DB

<a id="resq_mcp.pdie.service.get_vulnerability_map"></a>

#### get\_vulnerability\_map

```python
def get_vulnerability_map(sector_id: str) -> VulnerabilityMap | ErrorResponse
```

Retrieve precomputed vulnerability assessment for a sector.

Part of PDIE (Predictive Disaster Intelligence Engine) system.
Provides static infrastructure and risk data used as input to
predictive models for disaster forecasting.

Vulnerability Data Includes:
- Population density classification (low/medium/high)
- Critical infrastructure inventory (hospitals, bridges, etc.)
- Flood risk score (0.0-1.0) from terrain and drainage analysis
- Fire risk score (0.0-1.0) from fuel load and climate data

**Arguments**:

- `sector_id` - Sector identifier (e.g., "Sector-1" through "Sector-4").
  

**Returns**:

- `VulnerabilityMap` - Comprehensive vulnerability data if sector exists.
- `ErrorResponse` - Error message if sector_id is unknown.
  

**Example**:

  >>> vuln = get_vulnerability_map("Sector-1")
  >>> if isinstance(vuln, VulnerabilityMap):
  ...     if vuln.fire_risk > 0.7:
  ...         print(f"High fire risk: &#123;vuln.fire_risk&#125;")
  ...         print(f"Infrastructure: &#123;vuln.critical_infrastructure&#125;")
  

**Notes**:

  Production systems would integrate with GIS databases and update
  vulnerability maps periodically based on infrastructure changes
  and seasonal risk factors.

<a id="resq_mcp.pdie.service.get_predictive_alerts"></a>

#### get\_predictive\_alerts

```python
def get_predictive_alerts(sector_id: str) -> list[PreAlert] | ErrorResponse
```

Generate probabilistic disaster forecasts for a sector.

Part of PDIE system. Simulates the output of LSTM/GNN predictive models
that analyze weather patterns, sensor trends, and historical data to
forecast disasters before they occur.

Prediction Logic (Simulated):
- Checks vulnerability map for sector risk factors
- Fire alert: Triggered if fire_risk > 0.5 (40% probability)
- Probability: 0.75-0.95
- Horizon: 4-24 hours
- Flood alert: Triggered if flood_risk > 0.5 (40% probability)
- Probability: 0.80-0.95
- Horizon: 12-48 hours
- Returns empty list if no alerts generated

**Arguments**:

- `sector_id` - Sector identifier to generate forecasts for.
  

**Returns**:

- `list[PreAlert]` - Zero or more pre-alerts with disaster forecasts
  if sector is valid.
- `ErrorResponse` - Error message if sector_id is unknown.
  

**Example**:

  >>> alerts = get_predictive_alerts("Sector-1")
  >>> if isinstance(alerts, list):
  ...     for alert in alerts:
  ...         print(f"Predicted: &#123;alert.predicted_disaster_type&#125;")
  ...         print(f"Probability: &#123;alert.probability:.0%&#125;")
  ...         print(f"Time horizon: &#123;alert.forecast_horizon_hours&#125;h")
  
  Integration Note:
  Production PDIE would run continuously with:
  - Weather API integration (NOAA, MeteoBlue)
  - IoT sensor stream processing (water levels, smoke detectors)
  - Historical incident database for pattern matching
  - LSTM models for time-series forecasting
  - GNN models for spatial correlation analysis

<a id="resq_mcp.prompts"></a>

# resq\_mcp.prompts

MCP prompt templates for the ResQ server.

<a id="resq_mcp.prompts.re"></a>

## re

<a id="resq_mcp.prompts.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.prompts.mcp"></a>

## mcp

<a id="resq_mcp.prompts.incident_response_plan"></a>

#### incident\_response\_plan

```python
@mcp.prompt()
def incident_response_plan(incident_id: str) -> str
```

Generate a structured prompt template for incident response planning.

Provides a framework for AI agents or human operators to systematically
analyze incidents and develop comprehensive response plans using
available MCP tools and resources.

Template Sections:
1. Situation Summary: Analyze current state and severity
2. Asset Allocation: Review and assign available resources
3. Risk Assessment: Evaluate hazards and constraints

**Arguments**:

- `incident_id` - The incident identifier to analyze (e.g., "INC-123").
  

**Returns**:

- `str` - Formatted prompt template with:
  - Analysis instructions
  - Tool references (get_deployment_strategy, resq://drones/active)
  - Expected output format
  

**Example**:

  >>> prompt = incident_response_plan("INC-456")
  >>> # Use with LLM:
  >>> response = llm.complete(prompt)
  >>> # LLM will call tools and produce structured response
  
  Use Cases:
  - AI-assisted crisis coordination (Spoon OS agent)
  - Human operator decision support
  - Training scenario generation
  - Post-incident plan review
  
  Integration:
  Prompt references MCP tools and resources that the LLM can call:
  - get_deployment_strategy(incident_id) -> OptimizationStrategy
  - resq://drones/active -> Fleet status
  - Additional sector/swarm status tools as needed

<a id="resq_mcp.resources"></a>

# resq\_mcp.resources

MCP resource endpoints for the ResQ server.

<a id="resq_mcp.resources.FastMCPError"></a>

## FastMCPError

<a id="resq_mcp.resources.mcp"></a>

## mcp

<a id="resq_mcp.resources.simulations"></a>

## simulations

<a id="resq_mcp.resources.get_simulation_status"></a>

#### get\_simulation\_status

```python
@mcp.resource("resq://simulations/{sim_id}")
async def get_simulation_status(sim_id: str) -> str
```

Get the current status of a physics simulation job.

Resource endpoint that provides real-time simulation progress and results.
Supports SSE subscriptions for push notifications on state changes.

URI Pattern:
resq://simulations/&#123;sim_id&#125;

Subscription Behavior:
Clients can subscribe to this resource to receive automatic updates
when simulation state transitions (pending -> processing -> completed).
Server sends resource_updated notifications via SSE.

**Arguments**:

- `sim_id` - Unique simulation job identifier (e.g., "SIM-A1B2C3D4").
  

**Returns**:

- `str` - Formatted string with simulation details:
  - Simulation ID
  - Current status (pending/processing/completed)
  - Progress percentage (0-100%)
  - Result URL (NeoFS CID) when completed
  - Original request parameters
  

**Raises**:

- `FastMCPError` - If sim_id not found in simulation registry.
  

**Example**:

  Client workflow:
  1. Call run_simulation tool -> get sim_id
  2. Subscribe to resq://simulations/&#123;sim_id&#125;
  3. Receive updates as simulation progresses
  4. Fetch result_url when status=completed
  
  Response Format:
  Simulation ID: SIM-A1B2C3D4
- `Status` - processing
- `Progress` - 50%
- `Result` - N/A (or neofs://sim_results/SIM-xxx.json)
- `Parameters` - &#123;scenario_id: ..., sector_id: ..., ...&#125;

<a id="resq_mcp.resources.list_active_drones"></a>

#### list\_active\_drones

```python
@mcp.resource("resq://drones/active")
def list_active_drones() -> str
```

List currently deployed drones in the active fleet.

Resource endpoint providing real-time fleet status for operator awareness.
Shows current deployment locations, battery levels, and operational modes.

URI Pattern:
resq://drones/active

**Returns**:

- `str` - Formatted string with active drone details:
  - Drone identifier
  - Drone type/capability (Surveillance/Payload/Relay)
  - Operational status (ACTIVE/RETURNING/CHARGING)
  - Battery percentage
  - Current sector assignment
  
  Example Response:
  [Active Fleet Status]
  - DRONE-Alpha (Surveillance): ACTIVE | Battery 78% | Sector 4
  - DRONE-Beta (Payload): RETURNING | Battery 12% | Sector 2
  - DRONE-Gamma (Relay): ACTIVE | Battery 92% | Sector 4
  
  Use Cases:
  - Operator dashboard fleet overview
  - Resource availability checking before deployment
  - Low battery alert monitoring
  - Sector coverage assessment
  

**Notes**:

  Current implementation returns static mock data. Production would
  query live telemetry from MCP drone feed server and aggregate
  real-time positions, battery, and mission status.

<a id="resq_mcp.server"></a>

# resq\_mcp.server

ResQ MCP Server - Model Context Protocol server for disaster response coordination.

This module provides the main FastMCP server implementation for ResQ, offering:
- Simulation management via resources and tools
- Drone fleet status and deployment
- Incident validation and response planning

The server uses a lifespan context manager to manage background tasks for
simulation processing and notification delivery.

<a id="resq_mcp.server.asyncio"></a>

## asyncio

<a id="resq_mcp.server.contextlib"></a>

## contextlib

<a id="resq_mcp.server.logging"></a>

## logging

<a id="resq_mcp.server.time"></a>

## time

<a id="resq_mcp.server.asynccontextmanager"></a>

## asynccontextmanager

<a id="resq_mcp.server.TYPE_CHECKING"></a>

## TYPE\_CHECKING

<a id="resq_mcp.server.Any"></a>

## Any

<a id="resq_mcp.server.FastMCP"></a>

## FastMCP

<a id="resq_mcp.server.settings"></a>

## settings

<a id="resq_mcp.server.validate_environment"></a>

## validate\_environment

<a id="resq_mcp.server.setup_telemetry"></a>

## setup\_telemetry

<a id="resq_mcp.server.logger"></a>

#### logger

<a id="resq_mcp.server.MAX_SIMULATIONS"></a>

#### MAX\_SIMULATIONS

<a id="resq_mcp.server.MAX_INCIDENTS"></a>

#### MAX\_INCIDENTS

<a id="resq_mcp.server.MAX_MISSIONS"></a>

#### MAX\_MISSIONS

active missions per session

<a id="resq_mcp.server.COMPLETED_TTL_SECONDS"></a>

#### COMPLETED\_TTL\_SECONDS

evict completed sims after 5 minutes

<a id="resq_mcp.server.FAILED_TTL_SECONDS"></a>

#### FAILED\_TTL\_SECONDS

evict failed sims sooner

<a id="resq_mcp.server.INCIDENT_TTL_SECONDS"></a>

#### INCIDENT\_TTL\_SECONDS

evict rejected incident records after 1 hour

<a id="resq_mcp.server.CONFIRMED_INCIDENT_TTL_SECONDS"></a>

#### CONFIRMED\_INCIDENT\_TTL\_SECONDS

confirmed incidents retained for 24h

<a id="resq_mcp.server.MISSION_TTL_SECONDS"></a>

#### MISSION\_TTL\_SECONDS

evict stale mission records after 2h

<a id="resq_mcp.server.simulations"></a>

#### simulations

<a id="resq_mcp.server.incidents"></a>

#### incidents

<a id="resq_mcp.server.missions"></a>

#### missions

keyed by drone_id

<a id="resq_mcp.server.lifespan"></a>

#### lifespan

```python
@asynccontextmanager
async def lifespan(server: FastMCP) -> "AsyncGenerator[None, None]"
```

Lifespan context manager for the MCP server with background tasks.

Manages the lifecycle of background processing tasks that run for the
duration of the server. Ensures clean startup and shutdown with proper
task cancellation and resource cleanup.

Background Tasks Started:
- simulation_processor: Mock simulation state machine that transitions
simulations from pending -> processing -> completed and sends SSE
notifications to subscribed clients.

Lifecycle:
1. Startup: Log initialization, create background tasks
2. Running: Yield control to FastMCP server
3. Shutdown: Cancel tasks, suppress CancelledError, log shutdown

**Arguments**:

- `server` - The FastMCP server instance for notification dispatch.
  

**Yields**:

- `None` - Control returns to FastMCP for request handling.
  

**Notes**:

  In production, background tasks would interface with actual
  simulation clusters, message queues (Redis/RabbitMQ), and
  maintain persistent connections to drone telemetry streams.

<a id="resq_mcp.server.mcp"></a>

#### mcp

<a id="resq_mcp.server.simulation_processor"></a>

#### simulation\_processor

```python
async def simulation_processor(server: FastMCP) -> None
```

Background processor for simulation state transitions and notifications.

Polls for pending simulations every 2 s and spawns an independent async
task per simulation so that no single job's delay blocks the others.

State Machine:
pending    -> processing (immediate, 50% progress, task spawned)
processing -> completed  (after 3 s inside _process_simulation)
processing -> failed     (on server shutdown mid-run)

Notifications:
SSE resource update notifications are sent on each state transition.

**Notes**:

  Production would replace this with a real job queue integration
  (Celery / RQ) and Unity/Unreal Engine status polling.

<a id="resq_mcp.server.tools"></a>

## tools

<a id="resq_mcp.server.tools"></a>

## tools

<a id="resq_mcp.server.prompts"></a>

## prompts

<a id="resq_mcp.server.resources"></a>

## resources

<a id="resq_mcp.server.main"></a>

#### main

```python
def main() -> None
```

Console script entry point for the ResQ MCP server.

<a id="resq_mcp.telemetry"></a>

# resq\_mcp.telemetry

Telemetry setup for the ResQ MCP server.

Provides initialization hooks for OpenTelemetry tracing and metrics.
Currently operates in no-op mode with structured logging as a fallback.

Future integration path:
    1. Install: opentelemetry-api, opentelemetry-sdk, opentelemetry-exporter-otlp
    2. Configure TracerProvider with appropriate exporters
    3. Configure MeterProvider for Prometheus metrics
    4. Add trace decorators to key operations

<a id="resq_mcp.telemetry.annotations"></a>

## annotations

<a id="resq_mcp.telemetry.logging"></a>

## logging

<a id="resq_mcp.telemetry.TYPE_CHECKING"></a>

## TYPE\_CHECKING

<a id="resq_mcp.telemetry.settings"></a>

## settings

<a id="resq_mcp.telemetry.logger"></a>

#### logger

<a id="resq_mcp.telemetry.setup_telemetry"></a>

#### setup\_telemetry

```python
def setup_telemetry() -> None
```

Initialize OpenTelemetry tracing and metrics.

Currently operates in no-op mode. When DEBUG is enabled, logs the
initialization for visibility.

<a id="resq_mcp.telemetry.trace"></a>

#### trace

```python
def trace(name: str | None = None) -> Callable[[F], F]
```

Decorator stub for tracing function execution.

**Arguments**:

- `name` - Optional span name. Defaults to the function name.
  

**Returns**:

  A no-op decorator that returns the original function.
  

**Example**:

  @trace("custom.operation.name")
  def my_function():
  ...

<a id="resq_mcp.tools"></a>

# resq\_mcp.tools

Drone feed tools for the ResQ MCP server.

This module provides simulated drone feed functionality for development and testing.
It generates pseudo-random telemetry and analysis data for drone network sectors.

The simulation includes:
- 4 monitored sectors with predefined coordinates
- Random disaster scenario detection (fire, flood, medical, debris)
- Swarm status with variable battery and connectivity
- Drone deployment request handling

<a id="resq_mcp.tools.annotations"></a>

## annotations

<a id="resq_mcp.tools.random"></a>

## random

<a id="resq_mcp.tools.UTC"></a>

## UTC

<a id="resq_mcp.tools.datetime"></a>

## datetime

<a id="resq_mcp.tools.Final"></a>

## Final

<a id="resq_mcp.tools.Coordinates"></a>

## Coordinates

<a id="resq_mcp.tools.DeploymentStatus"></a>

## DeploymentStatus

<a id="resq_mcp.tools.DisasterScenario"></a>

## DisasterScenario

<a id="resq_mcp.tools.ErrorResponse"></a>

## ErrorResponse

<a id="resq_mcp.tools.NetworkStatus"></a>

## NetworkStatus

<a id="resq_mcp.tools.SectorAnalysis"></a>

## SectorAnalysis

<a id="resq_mcp.tools.SectorStatusSummary"></a>

## SectorStatusSummary

<a id="resq_mcp.tools.SwarmStatus"></a>

## SwarmStatus

<a id="resq_mcp.tools.DRONE_SECTORS"></a>

#### DRONE\_SECTORS

<a id="resq_mcp.tools.DISASTER_SCENARIOS"></a>

#### DISASTER\_SCENARIOS

<a id="resq_mcp.tools.scan_current_sector"></a>

#### scan\_current\_sector

```python
def scan_current_sector(
        sector_id: str = "Sector-1") -> SectorAnalysis | ErrorResponse
```

Scan a specific sector for anomalies using simulated drone sensors.

Simulates drone-based surveillance with probabilistic disaster detection.
In production, this would integrate with actual drone telemetry and
edge AI processing results from the MCP drone feed server.

Detection Logic:
- 30% probability of detecting a disaster scenario per scan
- Randomly selects from predefined disaster templates
- Generates NeoFS evidence URL for blockchain submission
- Returns "clear" status if no anomalies detected

**Arguments**:

- `sector_id` - The sector to scan ("Sector-1" through "Sector-4").
  Default is "Sector-1".
  

**Returns**:

- `SectorAnalysis` - Complete scan results with detection data and
  recommended actions if sector exists.
- `ErrorResponse` - Error message if sector_id is invalid.
  

**Example**:

  >>> result = scan_current_sector("Sector-2")
  >>> if isinstance(result, SectorAnalysis):
  ...     if result.status == "CRITICAL_ALERT":
  ...         print(f"Alert: &#123;result.detected_object&#125;")
  ...         print(f"Action: &#123;result.recommended_action&#125;")
  

**Notes**:

  This is a simulation function. Production deployment would replace
  random detection with actual ML model inference on drone imagery.

<a id="resq_mcp.tools.get_all_sectors_status"></a>

#### get\_all\_sectors\_status

```python
def get_all_sectors_status() -> NetworkStatus
```

Get the status of all monitored sectors in the surveillance network.

Aggregates scan results across all configured sectors to provide
network-wide situational awareness for operator dashboards.

**Returns**:

- `NetworkStatus` - Complete network status including:
  - Total sector count
  - Per-sector status summaries (detected objects, confidence)
  - Critical alert count for priority filtering
  - Timestamp of status generation
  

**Example**:

  >>> status = get_all_sectors_status()
  >>> print(f"Network: &#123;status.total_sectors&#125; sectors")
  >>> print(f"Critical Alerts: &#123;status.critical_alerts&#125;")
  >>> for sector_id, summary in status.sectors.items():
  ...     if summary.status == "CRITICAL_ALERT":
  ...         print(f"&#123;sector_id&#125;: &#123;summary.detected_object&#125;")
  

**Notes**:

  Calls scan_current_sector() for each sector, so inherits its
  simulation behavior (random detection).

<a id="resq_mcp.tools.get_drone_swarm_status"></a>

#### get\_drone\_swarm\_status

```python
def get_drone_swarm_status() -> SwarmStatus
```

Get the overall operational status of the drone swarm.

Provides fleet-wide health metrics for monitoring drone readiness
and availability. Used by operators to assess deployment capacity.

Simulation Behavior:
- Total drones: Fixed at 3 for development
- Active drones: Random 2-3 (some may be charging/maintenance)
- Average battery: Random 60-100% (simulated degradation)
- Network status: Always "operational" in dev mode

**Returns**:

- `SwarmStatus` - Fleet metrics including:
  - Total and active drone counts
  - Fleet-wide average battery percentage
  - Network connectivity status
  - Last sync timestamp (auto-generated)
  

**Example**:

  >>> swarm = get_drone_swarm_status()
  >>> if swarm.average_battery < 30:
  ...     print("WARNING: Low fleet battery")
  >>> print(f"&#123;swarm.active_drones&#125;/&#123;swarm.total_drones&#125; drones active")
  

**Notes**:

  Production would aggregate real telemetry from the MCP drone feed
  server, reporting actual battery, GPS lock, and link quality.

<a id="resq_mcp.tools.request_drone_deployment"></a>

#### request\_drone\_deployment

```python
def request_drone_deployment(
        sector_id: str,
        priority: str = "high") -> DeploymentStatus | ErrorResponse
```

Request deployment of a drone to a specific sector.

Simulates drone dispatch request handling with immediate assignment.
In production, this would interface with the drone control module
and mission planning system to allocate resources.

Simulation Behavior:
- Assigns random drone unit (UNIT-001 through UNIT-003)
- Generates random ETA (30-120 seconds)
- Always returns "deployed" status if sector valid

**Arguments**:

- `sector_id` - The target sector for deployment (e.g., "Sector-1").
- `priority` - Deployment urgency level. Higher priority missions
  preempt lower priority tasks. Valid values:
  - "low": Routine surveillance
  - "medium": Follow-up investigation
  - "high" (default): Active incident response
  - "critical": Immediate life-threatening situation
  

**Returns**:

- `DeploymentStatus` - Confirmation with assigned drone and ETA if
  sector is valid.
- `ErrorResponse` - Error message if sector_id is invalid.
  

**Example**:

  >>> status = request_drone_deployment("Sector-3", priority="critical")
  >>> if isinstance(status, DeploymentStatus):
  ...     print(f"Drone &#123;status.drone_id&#125; dispatched")
  ...     print(f"ETA: &#123;status.eta_seconds&#125; seconds")
  

**Notes**:

  Production would check drone availability, battery levels, and
  weather conditions before confirming deployment.

