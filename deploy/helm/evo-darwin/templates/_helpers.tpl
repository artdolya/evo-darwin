{{/*
Name of every resource in the chart: the release name.
Terraform installs the release as "evo-darwin".
*/}}
{{- define "evo-darwin.fullname" -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Labels that select the pods. They must not change between releases.
*/}}
{{- define "evo-darwin.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Labels added to every resource.
*/}}
{{- define "evo-darwin.labels" -}}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version }}
{{ include "evo-darwin.selectorLabels" . }}
app.kubernetes.io/version: {{ .Values.image.tag | toString | trunc 63 | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
